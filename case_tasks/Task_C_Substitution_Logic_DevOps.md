# Case Task C — Substitution Logic Development, Git Workflow, Jenkins and Docker

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** Prototype Substitution Logic | **Tools:** GitHub Copilot / ChatGPT, Git, Jenkins, Docker  

---

## 1. Prototype Specification: Substitution Logic

The central engineering innovation in Case 37 is the **Substitution Logic Engine**. When a customer adds an item that is out of stock (or becomes unavailable before packing), the system must suggest an alternative based on four strict rules:
1. **Category Invariance:** The candidate must belong to the exact same category (e.g., Dairy $\to$ Dairy, Staples $\to$ Staples).
2. **Price Tolerance Constraint:** The candidate price increase cannot exceed $\max(\Delta_{user}, \text{Price}_{original} \times 0.20)$. Unreasonable price jumps are blocked.
3. **Allergen & Dietary Safety:** If the customer specifies allergens (`tree-nut`, `gluten`, `dairy`, `egg`), any candidate matching those allergens is immediately filtered out.
4. **Preference-Weighted Ranking:** In-stock candidates are scored by matching preference tags (e.g., `#toned`, `#whole-wheat`, `#organic`), then by lowest absolute price differential.

---

## 2. AI Prompting Interaction Log (ChatGPT / GitHub Copilot)

During development, ChatGPT was prompted with role-based and few-shot constraints to generate the core substitution algorithm:

### 2.1 The Prompt
```
System Role: Senior Python Software Engineer specializing in e-commerce algorithmic pricing and retail fulfillment.
Context: Case 37 Online Grocery. We need a function `suggest_substitution(requested, catalog, ...)` using Python dataclasses.
Constraints:
1. Must be deterministic and immutable.
2. Must validate all inputs (reject negative price limits, non-Product instances).
3. Check in_stock status and stock quantity.
4. Match categories case-insensitively.
5. Strict allergen avoidance intersection.
6. Enforce 20% maximum price delta.
7. Return a Substitution dataclass with selected SKU, price difference, match score, and human-readable reason.
```

### 2.2 Human Engineering Review & Code Corrections

| AI Suggestion Component | Potential Flaw / Weakness Identified | Human Engineering Fix Applied |
| :--- | :--- | :--- |
| **Price Delta Check** | AI wrote: `if candidate.price < max_price: valid.append(...)` | **Flaw:** Allowed candidates with negative or zero prices (e.g., -₹50) to pass as valid.<br>**Fix:** Added check: `if item.price <= 0: continue` and validated input prices strictly. |
| **Allergen Intersection** | AI wrote: `if allergen in candidate.allergens:` | **Flaw:** Case-sensitive string matching failed when customer selected "Tree-Nut" and candidate had "tree-nut".<br>**Fix:** Converted all allergen sets to `.casefold()` for robust normalized set intersection. |
| **Tie-Breaking** | AI returned `valid[0]` arbitrarily. | **Flaw:** Non-deterministic ordering led to flaky tests across platforms.<br>**Fix:** Implemented 4-tuple sorting key: `(-matching_tags, abs(delta), delta, item.name.casefold())`. |

---

## 3. Git Version Control and Feature Branching Strategy

The repository follows standard Gitflow / GitHub trunk branching practices:
1. `main` (or `master`): Production-ready, deployable code protected from direct pushes.
2. `feature/substitution-logic`: Dedicated development branch where the dataclasses, substitution engine, and PyTest suites were authored.
3. `feature/web-cart-slot-ui`: Dedicated branch for Flask routes, SQLite models, and Bootstrap templates.

```
Git Workflow Progression:
[master] ------------*-----------------------*-------------> [Deploy v1.0.0]
                      \                     / (Pull Request + Code Review)
[feature/sub-logic]    *----*----*---------*
```

### Git Command History Executed:
```bash
git checkout -b feature/substitution-logic
git add grocery_app/substitution.py tests/test_substitution.py
git commit -m "feat(substitution): implement rule-based product substitution engine with allergen filters"
git checkout master
git merge --no-ff feature/substitution-logic -m "merge: pull request #1 substitution logic module verified"
```

---

## 4. Continuous Integration with Jenkins (`Jenkinsfile`)

The CI/CD pipeline is codified in the workspace [Jenkinsfile](file:///e:/Case37-Online-Grocery/Jenkinsfile). It defines 6 automated build stages:
1. **Checkout Source:** Clones the repository upon Git push webhook.
2. **Environment & Lint:** Installs isolated Python dependencies from `requirements.txt`.
3. **Execute Unit & Integration Tests:** Runs `pytest -v --cov=grocery_app --cov-fail-under=80`. Builds fail if coverage drops below 80%.
4. **Static Code Analysis (SonarQube):** Analyzes security hotspots, code smells, and duplicates.
5. **Build Docker Container:** Packages the verified application into an immutable container image `freshcart-grocery:v1.0.0`.
6. **Health & Sanity Verification:** Executes synthetic HTTP probe against `http://localhost:5000/health`.

---

## 5. Docker Containerization Architecture (`Dockerfile`)

The application is containerized using [Dockerfile](file:///e:/Case37-Online-Grocery/Dockerfile) based on `python:3.14-slim`.

### Line-by-Line Architectural Rationale:
- `FROM python:3.14-slim`: Minimalist Debian-based image reducing attack surface and container footprint (<150 MB).
- `ENV PYTHONUNBUFFERED=1`: Ensures stdout/stderr are immediately flushed to docker logs for real-time observability.
- `WORKDIR /app`: Creates standardized execution directory.
- `COPY requirements.txt . && RUN pip install --no-cache-dir -r requirements.txt`: Leverages Docker layer caching so dependencies are not re-downloaded when application code changes.
- `COPY grocery_app/ grocery_app/`: Copies verified web application.
- `EXPOSE 5000`: Documents default container ingress port.
- `HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:5000/health || exit 1`: Native Docker health probe guaranteeing zero-downtime container orchestration.
- `CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]`: Production server entrypoint binding to all container interfaces.
