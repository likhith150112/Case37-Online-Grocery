# Lab Experiment L1.4 — Formal Requirements Specification: 10 FRs and 5 NFRs (Before and After Testable Versions)

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** Requirements Engineering | **AI Tool:** ChatGPT  

---

## 1. Aim
To elicit, structure, and refine 10 Functional Requirements (FRs) and 5 Non-Functional Requirements (NFRs) for the Online Grocery Application, transforming vague stakeholder statements into objectively verifiable, testable software engineering specifications.

---

## 2. Functional Requirements (10 Items)

| Req ID | Before Version (Vague / Stakeholder Input) | After Version (Measurable, Testable Acceptance Criteria) | Verification Method |
| :---: | :--- | :--- | :--- |
| **FR-01** | The app should have delivery slots. | The customer shall select from available 2-hour delivery slots during checkout. Slots that reach maximum capacity (10 orders/slot) shall be marked `[FULL]` and disabled from selection. | End-to-end checkout test; slot capacity query test. |
| **FR-02** | If milk is missing, suggest something else. | When an item has `in_stock = False` or `stock_qty < cart_qty`, the system shall recommend candidates belonging to the identical category whose price does not exceed original price by $> 20\%$. | PyTest unit tests `test_02`, `test_06`. |
| **FR-03** | Let users accept or reject substitutes. | The cart and substitution UI shall provide explicit `Accept` and `Reject` buttons. Accepting replaces the unavailable SKU with the substitute SKU; rejecting removes the unavailable item. | Integration test `test_int_05`, `test_int_06`. |
| **FR-04** | Don't give nut milk to allergic people. | The substitution engine shall cross-reference customer allergen tags (`avoid_allergens`) against candidate metadata and exclude any intersecting candidate from suggestions. | PyTest unit test `test_05_allergen_avoidance`. |
| **FR-05** | Customers should be able to search groceries. | The catalog view shall filter products in real-time by name, category, and descriptive tags using case-insensitive substring matching (`GET /?q=<term>`). | Flask route test `test_int_03_search_functionality`. |
| **FR-06** | Allow changing quantities in cart. | The shopping cart shall allow customers to modify item quantities between 1 and 20 units and update line totals and order subtotal immediately. | Cart update test `POST /cart/update`. |
| **FR-07** | Delivery charges should be free for big orders. | If order subtotal $\ge ₹500.00$, delivery fee shall be set to ₹0.00; otherwise, a flat fee of ₹30.00 shall be added to the order total. | Boundary price verification (₹499 vs ₹500). |
| **FR-08** | Save orders in the database. | Placing an order shall generate an immutable `order_code` (`FC-YYYYMMDD-XXXX`), record customer details, selected slot, and item breakdown in SQLite. | Database integrity test inspecting `orders` table. |
| **FR-09** | Update inventory upon order confirmation. | Upon successful order placement, the system shall decrement `stock_qty` of fulfilled items in an ACID transaction, preventing inventory drops below 0. | Database concurrency test. |
| **FR-10** | Provide system monitoring status. | The system shall expose a `/health` endpoint returning JSON HTTP 200 indicating service status, database connectivity, catalog count, and UTC timestamp. | Automated probe test `GET /health`. |

---

## 3. Non-Functional Requirements (5 Items)

| NFR ID | Before Version (Subjective / Vague) | After Version (Quantitative, Measurable SLA) | Measurement Tool |
| :---: | :--- | :--- | :--- |
| **NFR-01** | The website must be fast. | The 95th percentile response latency for catalog browsing and substitution computation shall be $< 200\text{ ms}$ under a concurrent load of 50 users. | Python monitoring script (`monitor.py`). |
| **NFR-02** | The system must be reliable. | The application shall maintain an operational reliability of $\ge 98.0\%$ across 50 consecutive automated order runs with zero data loss. | Reliability test suite (`reliability_test.py`). |
| **NFR-03** | User data must be private. | No real customer PII (credit cards, phone numbers, passwords) shall be transmitted in unencrypted form, stored in plain logs, or shared with AI APIs. | SonarQube security scan and code audit. |
| **NFR-04** | The codebase must be maintainable. | The Python codebase shall achieve $\ge 80.0\%$ test coverage with zero SonarQube blocker/critical code smells. | PyTest Coverage (`pytest-cov`) & SonarQube. |
| **NFR-05** | The app must work on modern browsers. | The user interface shall render responsively on Chrome, Firefox, Edge, and mobile viewports ($375\text{px}$ to $1920\text{px}$) without horizontal scrollbars. | Headless Chrome viewport validation. |

---

## 4. Conclusion
Transforming informal stakeholder statements into structured FRs and NFRs with quantitative acceptance criteria eliminated ambiguity, ensured testability, and provided the exact specification baseline for the PyTest and Selenium test suites.
