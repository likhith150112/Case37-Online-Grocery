# Case Task D — Selenium Automated Order Flow, Synthetic Test Data and Defect Prediction

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** Testing & Defect Prediction | **Tools:** Selenium WebDriver, Chrome, PyTest  

---

## 1. Selenium End-to-End Browser Automation Flow

To validate the complete customer journey, automated browser testing was implemented in [tests/test_selenium_order_flow.py](file:///e:/Case37-Online-Grocery/tests/test_selenium_order_flow.py) using Selenium WebDriver with Google Chrome.

### 1.1 Automated Journey Steps:
```
1. Browser Launch (Chrome Headless)
   └── Navigates to http://127.0.0.1:5000/
2. Product Search & Catalog Filter
   └── Queries "milk" -> Locates out-of-stock SKU MIL-002 (Amul Taaza)
3. Cart Addition
   └── Clicks "Add (Sub)" -> Session updates cart count
4. Out-of-Stock Alert Detection
   └── Cart banner renders "Unavailable Items Detected in Basket!"
5. Substitution Review Navigation
   └── Clicks "Review Substitutions" -> Side-by-side comparison loaded
6. Intelligent Substitute Acceptance
   └── Clicks "Accept Substitute" -> Replaces MIL-002 with MIL-001 (Nandini Milk)
7. Delivery Slot Selection & Checkout
   └── Verifies capacity -> Selects Morning Slot (07:00 AM - 09:00 AM)
8. Order Confirmation
   └── Clicks "Confirm Order" -> Verifies #order-confirmation and order code
```

---

## 2. Synthetic Test Data Generation and Privacy Protection

In accordance with strict data protection guidelines and university academic integrity standards:
- **Zero Real Customer Data:** No real customer names, live phone numbers, private home addresses, or financial payment details are uploaded to ChatGPT or stored in git.
- **Controlled Synthetic Test Profiles:** Test datasets were programmatically synthesized using realistic regional Indian personas:

| Persona ID | Synthetic Name | Simulated Contact | Synthetic Delivery Address | Dietary / Allergen Tag | Test Target |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SYN-01** | Likhith Gowda | `9876543210` | 37, 5th Main, Kumaraswamy Layout, Bengaluru | Standard | Baseline happy path |
| **SYN-02** | Aarav Sharma | `9811122233` | 14, 2nd Cross, Indiranagar, Bengaluru | Gluten-Free | Atta substitution filter |
| **SYN-03** | Ananya Iyer | `9844455566` | 89, 7th Block, Jayanagar, Bengaluru | Vegan / Tree-Nut Allergy | Almond milk exclusion |
| **SYN-04** | Mohammed Zaid | `9877788899` | 42, Mosque Road, Frazer Town, Bengaluru | Standard | Evening slot capacity check |

---

## 3. Machine Learning Defect Prediction Model

Software defect prediction aims to identify error-prone modules before release by analyzing code complexity metrics.

### 3.1 Code Metric Extraction Across Modules

| Module File | Lines of Code (LOC) | Cyclomatic Complexity ($v(G)$) | Halstead Volume ($V$) | Code Churn (Revisions) | Defect Risk Score ($P_{defect}$) | Predicted Risk Level |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `grocery_app/substitution.py` | 185 | 14 | 1,420 | 6 | **0.78** | **High Risk** |
| `grocery_app/database.py` | 115 | 8 | 840 | 3 | **0.35** | **Medium Risk** |
| `grocery_app/app.py` | 260 | 18 | 2,150 | 8 | **0.82** | **High Risk** |
| `grocery_app/static/js/main.js`| 25 | 2 | 120 | 1 | **0.05** | **Low Risk** |

### 3.2 Logistic Defect Probability Formula:
$$P(\text{Defect}) = \frac{1}{1 + e^{-(-3.2 + 0.15 \times v(G) + 0.02 \times \text{Churn})}}$$

- For `substitution.py`: $v(G) = 14, \text{Churn} = 6 \implies P = \frac{1}{1 + e^{-(-3.2 + 2.10 + 0.12)}} = \frac{1}{1 + e^{0.98}} \approx 0.73$.
- **Action Taken:** Because `substitution.py` and `app.py` were predicted as high defect-probability modules, we instituted:
  1. Mandatory 85%+ PyTest code coverage.
  2. Targeted negative and boundary test cases (negative price caps, empty catalogs, allergy intersections).
  3. Pre-merge SonarQube static analysis.
