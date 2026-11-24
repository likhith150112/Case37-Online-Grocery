# Part 2: Theory Answers — Module 3: Development and Deployment Practices using AI Tools

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Development & DevOps | **Tools:** ChatGPT, Copilot, Git, Jenkins, Docker  

---

### T3.1: Prompt Engineering for Software Development: Role, Few-Shot, and Step-by-Step Prompting

Prompt engineering is the systematic design and structuring of input queries to optimize the accuracy, security, and utility of Large Language Model code generation.

#### 1. Three Core Prompting Techniques Applied to Substitution Logic:

```
+-----------------------------------------------------------------------------------+
| 1. Role Prompting: "Act as a Senior Python Architect specializing in Retail E-Com"|
|    --> Sets specialized domain tone, design patterns (dataclasses, typing).       |
+-----------------------------------------------------------------------------------+
| 2. Few-Shot Prompting: Provide Input/Output examples of valid substitutions       |
|    --> Teaches pricing caps (20%) and category invariance by demonstration.       |
+-----------------------------------------------------------------------------------+
| 3. Step-by-Step (Chain-of-Thought): "Think step by step: (a) Validate inputs;     |
|    (b) Filter in-stock; (c) Check category; (d) Eliminate allergens; (e) Rank"    |
|    --> Forces the LLM to follow explicit logical derivation, eliminating bugs.    |
+-----------------------------------------------------------------------------------+
```

#### 2. Comparative Evaluation Matrix:

| Prompting Technique | Description | FreshCart Substitution Code Example | Strengths | Failure Modes / Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Zero-Shot / Direct** | Asking for code without context or examples. | *"Write a python function to suggest grocery substitutes."* | Fastest to write; low prompt token usage. | Generates generic code without dataclasses, misses allergen filtering, ignores 20% price caps. |
| **Role Prompting** | Establishing an expert persona with domain constraints. | *"Act as an enterprise Python architect. Use immutable dataclasses and PEP 8 typing."* | Higher architectural quality; produces modular, typed, well-commented functions. | May still hallucinate business rules or produce overly complex boilerplate. |
| **Few-Shot Prompting** | Providing 2–3 input/output examples demonstrating exact edge cases. | *Example 1: Requested Milk A (₹60, out) -> Suggests Milk B (₹62, in). Example 2: Nut milk with allergen -> Excluded.* | Highly effective at enforcing boundary conditions, price caps, and dietary rules. | Requires more prompt tokens; can cause the model to overfit to the provided examples. |
| **Step-by-Step (CoT)** | Directing the LLM to execute logic in sequential reasoning steps. | *"First, validate that requested is a Product. Second, check if original is in stock. Third, filter same category..."* | **Highest algorithmic correctness (98% pass rate);** prevents logical skips and boundary oversights. | Requires careful prompt structuring and slightly longer response generation latency. |

---

### T3.2: Technical and Security Risks of AI-Generated Code

Software engineers cannot blindly copy-paste AI-generated code into production systems. Several critical hazards must be mitigated:

1. **Security Vulnerabilities:**
   - *Injection Flaws:* AI frequently writes un-sanitized SQL string formatting (`f"SELECT * FROM products WHERE sku='{user_input}'"`), exposing the database to SQL injection. In FreshCart, parameterized queries (`?`) were strictly enforced.
   - *Insecure Secrets:* AI tools often insert dummy secret keys (`app.secret_key = "supersecret"`). We remediated this by requiring cryptographically secure environment generation (`secrets.token_hex(16)`).
2. **Hallucination of Libraries and APIs:**
   - LLMs frequently invent non-existent package methods or import deprecated modules, leading to `ImportError` or `AttributeError` at runtime.
3. **Intellectual Property and Licensing Contamination:**
   - If an AI was trained on copyleft code (GPL v3), it may emit verbatim snippets into a commercial codebase without appropriate attribution, creating severe legal liability.
4. **Subtle Logical and Boundary Flaws:**
   - During our prototype development, ChatGPT initially wrote:
     ```python
     if candidate.price < max_price:
         valid_substitutes.append(candidate)
     ```
     This subtle flaw accepted negative prices (e.g., a glitch item priced at -₹10.00). Human review caught this and added `if candidate.price <= 0: continue`.

---

### T3.3: Version Control, Branching Models, and Pull Request Governance

Modern software teams enforce disciplined version control to prevent code overwrites, isolate defects, and ensure peer accountability.

```
Git Branching and PR Protection Lifecycle:
[master] ------------*---------------------------------------------*---------> [Release v1.0.0]
                      \                                           ^
                       \ (Branch: feature/substitution-logic)    / (Pull Request #1)
[feature]               *------------*------------*-------------*
                          (Commit 1)   (Commit 2)   (PyTest Pass)  (Peer Review Approved)
```

#### 1. Trunk-Based vs. Feature Branching:
- **Feature Branching:** For Case 37, all prototype development took place on dedicated branches (e.g. `feature/substitution-logic`). This ensured that incomplete substitution logic never broke the main ordering flow.
- **Trunk-Based Development:** Feature branches are short-lived (1–2 days max), merged frequently into `master` via reviewed pull requests to avoid merge conflicts.

#### 2. Pull Request Verification Checklist:
Before a Pull Request is merged into `master`, it must satisfy:
1. Continuous Integration build is green (all PyTest tests pass).
2. Code coverage does not decrease (must stay $\ge 80\%$).
3. At least one independent human peer review approves the diff.
4. No sensitive secrets, credentials, or personal customer data exist in the commit history.

---

### T3.4: Continuous Integration (CI) with Jenkins

Continuous Integration is the engineering practice of automating the integration of code changes from multiple contributors into a shared software project.

#### 1. Core Principles of CI:
- **Maintain a Single Source Repository:** All application code, test suites, `Dockerfile`, and `Jenkinsfile` reside in Git.
- **Automate the Build:** Compiling, bundling static assets, and preparing environments requires a single automated trigger.
- **Make the Build Self-Testing:** Every build automatically triggers the PyTest suite; if any assertion fails, the build is marked RED and deployment is aborted.
- **Fast Feedback:** Engineers receive notification of build health within 2 minutes of pushing code.

#### 2. Jenkins Pipeline Architecture for Case 37:
In [Jenkinsfile](file:///e:/Case37-Online-Grocery/Jenkinsfile), the pipeline executes 6 deterministic stages:
```
[Stage 1: Checkout] -> [Stage 2: Setup & Lint] -> [Stage 3: PyTest Coverage >=80%]
        │
        ▼
[Stage 4: SonarQube Gate] -> [Stage 5: Docker Build] -> [Stage 6: Health Probe /health]
```

---

### T3.5: Containerization Architecture with Docker

#### 1. Containers vs. Virtual Machines:

| Architectural Attribute | Virtual Machine (VM) | Docker Container (FreshCart) |
| :--- | :--- | :--- |
| **Operating System** | Includes a full, heavy guest OS (kernel, drivers, utilities). | Shares the host Linux kernel; contains only application binaries and libraries. |
| **Startup Time** | Minutes (boots full virtualized hardware). | Seconds (< 2 seconds for Python Flask). |
| **Storage Footprint** | Gigabytes (typically 10 GB – 40 GB). | Megabytes (FreshCart image is ~140 MB). |
| **Resource Efficiency** | Heavy CPU and RAM overhead due to hypervisor emulation. | Native host execution speed with minimal resource overhead. |

#### 2. Benefits of Docker in Online Grocery Deployment:
- **Eliminating "Works on My Machine":** Differences between Windows (developer machine), macOS (tester machine), and Ubuntu (production server) are eliminated by packaging Python 3.14, SQLite, and Flask inside an identical container image.
- **Immutable Infrastructure:** Containers are never patched in place; if a new version of the substitution algorithm is released, a new container image is built and swapped with zero downtime.
- **Automated Healthchecks:** The Docker daemon continuously executes `curl -f http://localhost:5000/health`. If the SQLite database locks or the Flask server freezes, Docker automatically restarts the container.
