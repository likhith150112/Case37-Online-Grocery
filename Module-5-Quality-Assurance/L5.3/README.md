# Lab Experiment L5.3 — Safe AI Code-Review Checklist Applied to Substitution Prototype

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Quality Assurance & Code Governance | **Reviewer:** Likhith Gowda M S  

---

## 1. Aim
To define a rigorous 7-point Safe AI Code-Review Checklist and systematically apply it to an AI-generated substitution code candidate prior to production integration.

---

## 2. Seven-Point Safe AI Code-Review Checklist

| Checklist Item | Review Question | Status | Reviewer Findings & Verification Evidence |
| :---: | :--- | :---: | :--- |
| **CHK-01** | **Requirement Compliance:** Does the generated code fulfill the approved functional requirement (FR-02 & FR-04)? | **[x] PASS** | Verified: Filters by matching category, enforces 20% price cap, and eliminates customer allergens. |
| **CHK-02** | **Input Validation:** Are all input parameters and data types strictly validated at function entry? | **[x] PASS** | Verified: Raises `TypeError` if `requested` is not `Product`; raises `ValueError` if thresholds $< 0$. |
| **CHK-03** | **Boundary & Negative Tests:** Are edge cases (zero price, empty catalog, negative caps) handled and tested? | **[x] PASS** | Verified: PyTest tests `test_03`, `test_06`, `test_08`, `test_10` pass cleanly. |
| **CHK-04** | **Data Privacy (Zero PII):** Does the code exclude personal customer identities, passwords, or tokens? | **[x] PASS** | Verified: Dataclasses operate strictly on SKU, price, category, and tags. Zero customer PII processed. |
| **CHK-05** | **Security & Injection:** Are database queries parameterized and protected against SQL injection? | **[x] PASS** | Verified: All SQLite queries in `database.py` use parameter placeholders (`?`). |
| **CHK-06** | **Licensing & Dependencies:** Are external libraries minimal, compatible, and free of copyleft restrictions? | **[x] PASS** | Verified: Uses standard Python library (`dataclasses`, `sqlite3`, `urllib`) + permissive BSD Flask. |
| **CHK-07** | **Human Review & Execution:** Has a human engineer read, executed, and verified every line locally? | **[x] PASS** | Verified: Executed locally by student Likhith Gowda M S on Python 3.14; 21/21 tests passed. |

---

## 3. Review Decision Log
- **AI Suggestion Target:** Substitution ranking function with price delta cap.
- **Review Date:** 24-November-2026  
- **Reviewer:** Likhith Gowda M S (Student / Lead Engineer)  
- **Final Verdict:** **APPROVED FOR MERGE TO MASTER** after implementing input type guard (CHK-02) and normalized set intersection (CHK-03).
