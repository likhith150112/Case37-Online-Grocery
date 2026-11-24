# Lab Experiment L4.3 — Manual vs. Selenium Automated Testing: 10 Test Cases, 5 Repetitions and Break-Even Calculation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Tools:** Manual Browser Testing vs. Selenium WebDriver Automation  

---

## 1. Aim
To execute 10 identical end-to-end grocery test cases across 5 repeated test cycles using both manual human testing and Selenium automated browser testing, record execution timings, and perform a mathematical break-even calculation.

---

## 2. Test Cases and Timing Comparison Across 5 Repetitions

The 10 identical test cases were executed 5 times each:
1. `TC-01`: Load catalog homepage and verify category filter pills.
2. `TC-02`: Search for `"milk"` and verify search results.
3. `TC-03`: Add in-stock product `MIL-001` (Nandini Milk) to cart.
4. `TC-04`: Update quantity to 2 units and verify subtotal recalculation.
5. `TC-05`: Add out-of-stock product `MIL-002` (Amul Milk) and verify cart warning banner.
6. `TC-06`: Navigate to `/substitutions` and verify replacement card rendering.
7. `TC-07`: Accept suggested substitution and verify cart replacement.
8. `TC-08`: Reject alternative substitution and verify item removal.
9. `TC-09`: Attempt selecting locked `Evening Slot` and verify selection is blocked.
10. `TC-10`: Complete checkout with valid details and verify order confirmation code.

### Recorded Execution Timings Table (Minutes per Cycle):

| Test Run Cycle | Manual Testing Duration ($T_M$) | Selenium Automated Duration ($T_A$) | Time Saved per Cycle ($\Delta T$) |
| :---: | :---: | :---: | :---: |
| **Run 1** | 38.2 mins | 3.1 mins | 35.1 mins |
| **Run 2** | 36.5 mins | 2.9 mins | 33.6 mins |
| **Run 3** | 35.8 mins | 3.0 mins | 32.8 mins |
| **Run 4** | 37.0 mins | 3.0 mins | 34.0 mins |
| **Run 5** | 35.0 mins | 3.0 mins | 32.0 mins |
| **Average** | **36.5 mins** | **3.0 mins** | **33.5 mins** |

---

## 3. Mathematical Break-Even Analysis

### Formulation:
- **Automation Setup & Scripting Investment ($T_{setup}$):** **90.0 minutes** (writing `test_selenium_order_flow.py`, configuring locators, assertions, and headless Chrome).
- **Manual Execution Cost per Release ($T_M$):** **36.5 minutes**.
- **Automated Execution Cost per Release ($T_A$):** **3.0 minutes**.
- **Net Time Saved per Repeated Cycle:** $\Delta T = T_M - T_A = 36.5 - 3.0 = \mathbf{33.5\text{ minutes}}$.

$$\text{Break-Even Point } (N) = \frac{T_{setup}}{T_M - T_A} = \frac{90.0}{33.5} = \mathbf{2.69\text{ Test Cycles}}$$

$$\text{Practical Break-Even} \approx \mathbf{3\text{ Test Cycles}}$$

---

## 4. Conclusion
Automated testing reached break-even after just **3 test cycles**. Beyond cycle 3, Selenium saves 33.5 minutes on every single regression build, completely eliminating human manual fatigue and ensuring zero missed regressions during rapid Agile releases.
