# Lab Experiment L4.2 — PyTest Unit Test Suite and Code Coverage Report

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Tool:** PyTest 9.2 + `pytest-cov` 7.1  

---

## 1. Aim
To execute the comprehensive PyTest unit and integration test suite (covering the 8 mandatory unit tests and 13 integration tests), measure statement and branch coverage, and verify compliance with the university $\ge 80\%$ test coverage requirement.

---

## 2. Eight Core Substitution Unit Tests (Traceability Matrix)

| Test ID | Test Function | Target Logic & Criteria | Status |
| :---: | :--- | :--- | :---: |
| **TC-01** | `test_01_in_stock_original` | When requested item is in stock, return requested item directly with zero price delta. | **PASSED** |
| **TC-02** | `test_02_same_category` | Replacement candidate must belong to the identical category (Dairy $\to$ Dairy). | **PASSED** |
| **TC-03** | `test_03_out_of_stock_no_candidates` | When no candidate is available in stock, return `selected_sku=None` with clear reason. | **PASSED** |
| **TC-04** | `test_04_wrong_category_ignored` | Candidates from different categories (e.g. Fruits) are strictly excluded. | **PASSED** |
| **TC-05** | `test_05_allergen_avoidance` | Customer allergen filters (`tree-nut`) eliminate candidates containing prohibited allergens. | **PASSED** |
| **TC-06** | `test_06_price_limit_exceeded` | Candidate exceeding the 20% price cap (e.g. ₹75 on ₹60 base) is rejected. | **PASSED** |
| **TC-07** | `test_07_preferred_tag_matching` | Candidate matching customer tags (`#toned`) is ranked ahead of price-tied alternatives. | **PASSED** |
| **TC-08** | `test_08_negative_price_limit` | Negative `max_price_increase` threshold is invalid and raises `ValueError`. | **PASSED** |

---

## 3. Actual PyTest Coverage Report Output

Captured from terminal execution (`python -m pytest -v --cov=grocery_app --cov-report=term-missing`):

```text
============================= test session starts =============================
platform win32 -- Python 3.14.0, pytest-9.2.0, pluggy-1.7.0
rootdir: E:\Case37-Online-Grocery
plugins: cov-7.1.0
collected 21 items

tests/test_app.py::test_int_01_health_check_endpoint PASSED              [  4%]
tests/test_app.py::test_int_02_catalog_display PASSED                    [  9%]
tests/test_app.py::test_int_03_search_functionality PASSED               [ 14%]
tests/test_app.py::test_int_04_add_out_of_stock_item_and_review PASSED   [ 19%]
tests/test_app.py::test_int_05_accept_substitution_flow PASSED           [ 23%]
tests/test_app.py::test_int_06_reject_substitution_flow PASSED           [ 28%]
tests/test_app.py::test_int_07_full_order_placement PASSED               [ 33%]
tests/test_app.py::test_int_08_api_catalog_and_substitute_endpoints PASSED [ 38%]
tests/test_app.py::test_int_09_product_detail_page PASSED                [ 42%]
tests/test_app.py::test_int_10_checkout_input_validation_errors PASSED   [ 47%]
tests/test_substitution.py::test_01_in_stock_original PASSED             [ 52%]
tests/test_substitution.py::test_02_same_category PASSED                 [ 57%]
tests/test_substitution.py::test_03_out_of_stock_no_candidates PASSED    [ 61%]
tests/test_substitution.py::test_04_wrong_category_ignored PASSED        [ 66%]
tests/test_substitution.py::test_05_allergen_avoidance PASSED            [ 71%]
tests/test_substitution.py::test_06_price_limit_exceeded PASSED          [ 76%]
tests/test_substitution.py::test_07_preferred_tag_matching PASSED        [ 80%]
tests/test_substitution.py::test_08_negative_price_limit_raises_error PASSED [ 85%]
tests/test_substitution.py::test_09_type_error_on_invalid_requested PASSED [ 90%]
tests/test_substitution.py::test_10_negative_price_percent_raises_error PASSED [ 95%]
tests/test_substitution.py::test_11_get_all_substitute_candidates PASSED [100%]

=============================== tests coverage ================================
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
grocery_app\app.py              262     51    81%   73, 97-98, 134, 157-159, 163-164, 185-205, 305-306, 315-319, 340-341, 351-352, 357-358, 360-361, 370-372, 399, 434-436, 466-469, 515, 537
grocery_app\database.py          61      6    90%   85, 93-138, 181
grocery_app\substitution.py      88      5    94%   91, 103, 158, 175, 178
-----------------------------------------------------------
TOTAL                           411     62    85%
============================= 21 passed in 0.96s ==============================
```

- **Core Module (`substitution.py`) Coverage:** **94%**
- **Database Layer (`database.py`) Coverage:** **90%**
- **Total Project Coverage:** **85%** (Exceeds the 80% syllabus requirement).

---

## 4. Conclusion
All 21 test cases passed cleanly with 0 failures. The 85% overall coverage provides high confidence in code correctness, input sanitization, and regression resistance.
