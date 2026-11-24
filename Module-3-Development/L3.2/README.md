# Lab Experiment L3.2 — Working Substitution Prototype with Accepted and Rejected AI Suggestion Log

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Development & Code Review | **AI Tool:** ChatGPT / GitHub Copilot  

---

## 1. Aim
To execute and document the working Substitution Logic Prototype, recording a formal engineering audit log of all AI code suggestions, explicitly detailing which suggestions were accepted, which were rejected, and why.

---

## 2. Working Prototype Execution Output

Executing the prototype module (`grocery_app/substitution.py`):
```text
=== FreshCart Substitution Logic Prototype Execution ===
Simulated Customer Basket:
- Requested SKU: MIL-002 (Amul Taaza Homogenised Milk 1L)
- Status: OUT OF STOCK (0 units available)
- Category: Dairy | Base Price: ₹54.00 | Avoid Allergens: ()

Evaluating Candidates in Catalog:
1. Candidate: MIL-001 (Nandini Toned Fresh Milk 1L)
   - Category: Dairy [MATCH]
   - In Stock: True (25 units) [PASS]
   - Price: ₹44.00 (Delta: -₹10.00, <= 20% limit) [PASS]
   - Allergens: None [PASS]
   - Score: 0.81

2. Candidate: MIL-003 (Mother Dairy Full Cream Milk 1L)
   - Category: Dairy [MATCH]
   - In Stock: True (15 units) [PASS]
   - Price: ₹66.00 (Delta: +₹12.00, exceeds ₹10.80 limit) [FAIL - PRICE CEILING]

Top Recommended Substitute:
-> Selected SKU: MIL-001 (Nandini Toned Fresh Milk 1L)
-> Price Difference: -₹10.00 (Customer saves ₹10.00)
-> Status: Awaiting Explicit Customer Acceptance
```

---

## 3. Audit Log of Accepted and Rejected AI Suggestions

| Suggestion ID | AI Proposed Code Snippet | Engineering Verdict | Detailed Technical Reason |
| :---: | :--- | :---: | :--- |
| **AI-SUG-01** | Use Python `@dataclass(frozen=True)` for `Product` and `Substitution`. | **ACCEPTED** | Enforces immutability, prevents accidental modification of stock during sorting, and provides clean hashability. |
| **AI-SUG-02** | `if candidate.price < max_price:` | **REJECTED** | **Severe Bug:** Accepted negative prices (e.g. -₹50) as valid candidates. Replaced with `if candidate.price <= 0: continue`. |
| **AI-SUG-03** | Use set intersection for allergen exclusion: `blocked.intersection(item.allergens)`. | **ACCEPTED (Modified)** | Excellent mathematical performance ($O(1)$ lookup), but modified with `.casefold()` to prevent case-sensitivity misses. |
| **AI-SUG-04** | Use recursive retry if no substitute found in same category to check related categories. | **REJECTED** | **Safety Violation:** Recommending a bakery item when dairy is out of stock violates core grocery domain rules. Category invariance must be absolute. |
| **AI-SUG-05** | Return `Substitution` dataclass with `match_score` float between 0.0 and 1.0. | **ACCEPTED** | Provides quantitative match quality displayed as percentage badge in the UI. |

---

## 4. Conclusion
The prototype audit demonstrates that AI suggestions accelerate initial drafting, but human engineering review is vital to prevent business logic violations (e.g. cross-category substitution) and pricing bugs.
