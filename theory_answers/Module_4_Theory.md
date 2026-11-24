# Part 2: Theory Answers — Module 4: AI-Based Testing and Monitoring

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Testing & Continuous Monitoring | **Tools:** PyTest, Selenium, Synthetic Probes  

---

### T4.1: The Four Levels of Software Testing Applied to Online Grocery

Software testing is organized hierarchically to detect faults as close to their point of origin as possible, minimizing remediation cost.

```
+-----------------------------------------------------------------------------------+
|                         Acceptance Testing (UAT)                                  |
| (Store staff and customers validate delivery slot booking and substitute approval)|
+-----------------------------------------------------------------------------------+
                                         ▲
+-----------------------------------------------------------------------------------+
|                           System Testing (E2E)                                    |
| (Selenium browser automation from catalog search to checkout and order confirm)   |
+-----------------------------------------------------------------------------------+
                                         ▲
+-----------------------------------------------------------------------------------+
|                           Integration Testing                                     |
| (Flask HTTP routes, session cart state, and SQLite ACID transaction persistence)   |
+-----------------------------------------------------------------------------------+
                                         ▲
+-----------------------------------------------------------------------------------+
|                              Unit Testing                                         |
| (PyTest testing pure mathematical functions: suggest_substitution, price deltas)  |
+-----------------------------------------------------------------------------------+
```

#### Detailed Definitions and Grocery Examples:

1. **Unit Testing:** Tests individual functions or classes in complete isolation from external databases or networks. Example: `test_01_in_stock_original` in `tests/test_substitution.py` verifies that if an item is in stock, `suggest_substitution` returns the exact requested SKU with ₹0.00 delta.
2. **Integration Testing:** Tests interactions between collaborating software modules. Example: `test_int_05_accept_substitution_flow` in `tests/test_app.py` verifies that accepting a substitute updates the Flask user session cart and correctly renders the modified item in SQLite.
3. **System Testing (End-to-End):** Validates the entire integrated application against functional and non-functional requirements in an environment simulating real customer usage. Example: Selenium WebDriver executing an automated browser session navigating from catalog browse, to substitution review, to delivery slot reservation, to order confirmation.
4. **Acceptance Testing (UAT):** Conducted by business stakeholders (Store Managers, Order Pickers, and Beta Shoppers) to ensure the system satisfies real-world commercial needs (e.g., ensuring evening slots are never double-booked).

---

### T4.2: Black-Box vs. White-Box Test Design Techniques

#### 1. Black-Box Testing (Specification-Based):
Black-box testing derives test cases purely from requirements specifications without knowledge of internal code paths.

- **Equivalence Partitioning (EP):** Inputs are divided into valid and invalid classes.
  - *Valid Partition:* Price delta $\le 20\%$ of base price (e.g. Base = ₹100, Candidate = ₹115 $\to$ ACCEPT).
  - *Invalid Partition:* Price delta $> 20\%$ of base price (e.g. Base = ₹100, Candidate = ₹125 $\to$ REJECT).
- **Boundary Value Analysis (BVA):** Defects concentrate at boundaries between partitions.
  - For a base price of ₹100 with a $20\%$ cap (Limit = ₹120.00):
    - *Nominal Boundary:* Candidate = ₹120.00 (Boundary Pass).
    - *Above Boundary:* Candidate = ₹120.01 (Boundary Fail).
    - *Below Boundary:* Candidate = ₹119.99 (Boundary Pass).
- **Decision Table Testing:** Maps complex combinations of conditions (Category Match, In Stock, Allergen Flag, Price $\le$ Cap) to expected substitution outputs.

#### 2. White-Box Testing (Structure-Based):
White-box testing derives test cases from internal source code logic and control flow graphs.
- **Statement Coverage:** Ensures every line of Python code executes at least once. (FreshCart achieved $85\%$ statement coverage).
- **Branch / Decision Coverage:** Verifies that both True and False outcomes of every `if` condition (e.g., `if requested.in_stock:`) are tested.
- **Path Coverage:** Ensures all independent linear paths through nested loops and conditional branches execute without uncaught exceptions.

---

### T4.3: Automated vs. Manual Testing and Break-Even Analysis

While manual testing is essential for exploratory, visual, and heuristic assessments, automated testing provides unmatched regression speed and repeatability.

#### Mathematical Break-Even Analysis Formula:
$$N = \frac{\text{Initial Automation Setup Time}}{\text{Manual Test Execution Time} - \text{Automated Test Execution Time}}$$

#### FreshCart Empirical Measurement Data (10 Test Cases, 5 Repetitions):
- Manual execution time per full cycle ($T_{manual}$): **36.5 minutes** (browsing, typing inputs, verifying screens).
- Automated Selenium execution time per full cycle ($T_{auto}$): **3.0 minutes** (runs headlessly in background).
- Initial setup & scripting time ($T_{setup}$): **90.0 minutes**.
- Time saved per test cycle: $36.5 - 3.0 = \mathbf{33.5\text{ minutes}}$.
- **Break-Even Point ($N$):**
  $$N = \frac{90.0}{33.5} \approx \mathbf{2.69\text{ test cycles}}$$

**Conclusion:** After just **3 regression cycles**, automated testing fully recovers its development investment and continues to save 33.5 minutes on every subsequent release.

---

### T4.4: AI in Test Case Generation and Test Data Privacy

#### 1. AI Capabilities in Test Engineering:
- **Boundary and Negative Case Discovery:** ChatGPT identifies overlooked negative paths (e.g., what happens if a product has price ₹0.00, negative quantity, or an empty category string?).
- **Synthetic Test Data Generation:** AI synthesizes realistic product catalogs, address formats, and diverse customer personas without requiring manual data entry.

#### 2. Strict Privacy Principles in Academic & Enterprise Testing:
Software quality assurance must adhere to strict data protection standards (GDPR, DPDP Act 2023):
- **Never Upload Real PII:** Real customer phone numbers, home addresses, payment tokens, or passwords must never be used in AI test prompts.
- **Pseudonymization and Synthetic Personas:** Use standardized synthetic profiles (e.g. *Likhith Gowda, 9876543210, No. 37 Kumaraswamy Layout*).
- **Zero Sensitive Data in Source Repositories:** Git pre-commit hooks and `.gitignore` ensure test logs with environment tokens are never pushed to GitHub.

---

### T4.5: Continuous Health Monitoring, Synthetic Probes, and Alerting

Continuous monitoring bridges the gap between pre-release testing and live operational reliability.

```
Monitoring Pipeline Architecture:
[Synthetic Cron Probe] ──(HTTP GET /health every 60s)──> [FreshCart Flask Server]
                                                                │
                                                                ▼
                                                        [Query SQLite DB]
                                                                │
                 ┌──────────────────────────────────────────────┴──────────────────────────────┐
                 ▼ (Latency <= 2.0s & DB UP)                                                   ▼ (Latency > 2.0s or DB DOWN)
       [Log: 200 OK Status]                                                          [TRIGGER SYSTEM ALERT]
       [Append to monitor.log]                                                       [Log: ALERT: slow response / DB DOWN]
```

#### Key Monitoring Parameters in FreshCart (L4.5):
1. **Health Check Endpoint (`/health`):** A dedicated lightweight REST route querying SQLite database connectivity, active catalog count, and server uptime.
2. **Threshold Monitoring:** If response latency exceeds **2.0 seconds** (`THRESHOLD_SECONDS = 2.0`), an automatic `ALERT: slow response` is logged.
3. **Heartbeat Probing:** A background script probes the server every minute for 10 minutes, generating real-time response time trend logs and graphs.
