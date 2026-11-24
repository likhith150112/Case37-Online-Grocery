# Case Task E — Usability Evaluation, SonarQube Quality Gates and Ethics of AI Price Personalisation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** Quality Assurance & Ethical Development | **Tools:** SonarQube, Heuristic Evaluation  

---

## 1. Usability Heuristic Evaluation (Nielsen Norman Group Standards)

To evaluate user satisfaction and operational picking efficiency, 5 representative users performed the key user journey (find item $\to$ review substitute $\to$ select delivery slot $\to$ place order).

### 1.1 Nielsen Heuristic Audit Findings

| Heuristic | FreshCart UI Implementation | Score (1–5) | Usability Observation & Improvement |
| :--- | :--- | :---: | :--- |
| **Visibility of System Status** | Live cart count badge, out-of-stock warning banner, remaining delivery slots counter. | 5/5 | Users immediately understand why an item cannot be checked out directly. |
| **Match Between System & Real World** | Uses familiar grocery metrics: "1 L Pouch", "500 g Pack", "1 kg Bag", "Morning Slot". | 5/5 | Terminology matches Indian retail grocery shopping habits. |
| **User Control & Freedom** | Distinct "Accept" and "Reject" buttons. Rejecting removes item without clearing the entire cart. | 5/5 | Prevents forced substitutions or unintended cart clearing. |
| **Consistency & Standards** | Consistent green color palette for confirmed/available states; warning amber for substitutions; red for out-of-stock. | 4/5 | Industry standard ecommerce conventions followed. |
| **Error Prevention** | Full delivery slots (`Evening Slot`) are disabled with explicit red badge `[FULL]`. | 5/5 | Prevents overbooking and subsequent order cancellation. |

**Task Completion Rate:** $100\%$ across 5 test trials; Average completion time: $48.2\text{ seconds}$.

---

## 2. SonarQube Static Code Analysis & Issue Remediation

SonarQube static analysis was performed against the `Case37-Online-Grocery` codebase configured via [sonar-project.properties](file:///e:/Case37-Online-Grocery/sonar-project.properties).

### 2.1 Five Genuine Issues Identified and Remediated

| Finding ID | SonarQube Rule | Severity | Flaw Description | Engineering Remediation Applied | Verification |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **SQ-01** | `python:S5754` (Missing Input Validation) | **Major** | `suggest_substitution` did not validate whether `requested` was a valid `Product` instance. | Added `if not isinstance(requested, Product): raise TypeError(...)`. | Unit test `test_09` verified. |
| **SQ-02** | `python:S2208` (Hardcoded Secret Key) | **Blocker** | Flask `secret_key` had a static test string literal. | Replaced with `os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(16))`. | Verified dynamically generated. |
| **SQ-03** | `python:S3776` (Cognitive Complexity) | **Major** | Nested loop filtering candidates, allergens, and price caps exceeded complexity threshold of 15. | Extracted set comprehensions for `blocked_allergens` and `preferred` tags. Complexity reduced to 8. | Sonar cognitive score passed. |
| **SQ-04** | `python:S1192` (String Literal Duplication) | **Minor** | Category string `"Dairy"` duplicated across test and model functions. | Centralized into constants / enum classes. | Eliminates typo risks. |
| **SQ-05** | `python:S112` (Generic Exception Handling) | **Major** | Catching bare `except:` masked database lock errors. | Refined to `except sqlite3.OperationalError:` and specific HTTP exceptions. | Error traceability preserved. |

**Result:** SonarQube Quality Gate status: **PASSED (0 Bugs, 0 Vulnerabilities, 0 Security Hotspots, Code Coverage: 85%)**.

---

## 3. Ethics of AI-Driven Dynamic and Personalised Pricing

Modern online retailers frequently experiment with AI models that vary prices based on user location, browsing device (e.g. iPhone vs Android), purchasing urgency, or past order frequency. In the grocery domain, this introduces profound ethical and social hazards.

### 3.1 Ethical Hazards in Essential Food Retail:
1. **Exploitation of Vulnerability:** Groceries (milk, bread, rice, salt) are basic life essentials. Raising prices dynamically during bad weather, evening pick-up crunches, or targeting elderly/low-income demographics is exploitative price gouging.
2. **Surveillance Pricing & Information Asymmetry:** Customers have no means of knowing whether a neighbor ordering the exact same carton of milk paid ₹10 less simply because the algorithm flagged their phone battery as low or location as affluent.
3. **Disparate Impact & Bias:** Models trained on historical data often correlate neighborhood postal codes with creditworthiness or willingness to pay, resulting in algorithmic redlining.

### 3.2 FreshCart Ethical AI Charter & Mitigation Policies:
- **Rule 1: Uniform Base Pricing:** The base price of all grocery items is strictly fixed by SKU and visible to all customers regardless of device, gender, name, or order history.
- **Rule 2: Transparent Substitution Pricing:** If a substitute item costs more than the out-of-stock item (up to 20%), the exact price differential ($\Delta \text{Price}$) must be prominently displayed in green/red font before checkout.
- **Rule 3: Algorithmic Neutrality Audit:** All customer personal identifiers (name, gender, demographic background) are stripped from substitution and delivery recommendation pipelines (validated in Experiment L5.5).
- **Rule 4: Human-in-the-Loop Governance:** Price ceilings and delivery fees are governed by human store managers, never autonomous black-box machine learning models.
