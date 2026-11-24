# Lab Experiment L4.4 — Risk-Based Testing: Likelihood and Impact Scoring for Test Prioritization

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Methodology:** Risk-Based Testing (RBT)  

---

## 1. Aim
To evaluate and score 10 software testing scenarios in the Online Grocery Application using a quantitative Likelihood (1–5) and Impact (1–5) risk matrix, selecting the top 5 highest-risk tests to prioritize in CI/CD pipeline execution.

---

## 2. Risk Scoring Formula and Evaluation Scale
$$\text{Risk Exposure Score (RES)} = \text{Likelihood of Failure (L)} \times \text{Business Impact of Failure (I)}$$

- **Likelihood (1 to 5):** 1 = Very Rare; 3 = Moderate / Frequent code changes; 5 = Highly Complex / Concurrency prone.
- **Impact (1 to 5):** 1 = Minor cosmetic blemish; 3 = Annoying user friction; 5 = Catastrophic (financial loss, food allergy liability, legal breach).

---

## 3. Risk Scoring Matrix for Ten Grocery Scenarios

| Rank | Test Scenario Description | Likelihood (L) | Impact (I) | Risk Score ($L \times I$) | Risk Priority | Selected for Top 5 CI Suite? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **Allergen Contamination in Substitute:** Recommending nut or gluten product to allergic customer. | 4 | 5 | **20** | **Critical (P1)** | **YES (Top 1)** |
| **2** | **Delivery Slot Overbooking:** Multiple concurrent users booking final slot, leading to unfulfilled delivery. | 4 | 5 | **20** | **Critical (P1)** | **YES (Top 2)** |
| **3** | **Unbounded Price Escalation:** Recommending replacement exceeding 20% price cap, causing billing disputes. | 4 | 4 | **16** | **High (P2)** | **YES (Top 3)** |
| **4** | **Inventory Concurrency Race Condition:** Double-selling last carton of milk during peak morning rush. | 3 | 5 | **15** | **High (P2)** | **YES (Top 4)** |
| **5** | **Order Database Persistence Failure:** Customer receives confirmation but order is lost in backend DB. | 3 | 4 | **12** | **High (P2)** | **YES (Top 5)** |
| 6 | Cross-Category Replacement: Suggesting cooking oil when rice is unavailable. | 2 | 4 | 8 | Medium (P3) | No |
| 7 | Search Typo Handling: Substring search fails on minor spelling variants. | 3 | 2 | 6 | Medium (P3) | No |
| 8 | Cart Quantity Dropdown Overflow: User attempts ordering 25 units when max is 20. | 2 | 2 | 4 | Low (P4) | No |
| 9 | UI Category Pill Hover Color Mismatch: Cosmetic CSS style glitch on hover. | 2 | 1 | 2 | Low (P4) | No |
| 10 | Footer Copyright Year Display: Hardcoded year in static template. | 1 | 1 | 1 | Trivial (P5) | No |

---

## 4. Top 5 Prioritized High-Risk Test Execution Plan

The top 5 tests (Risk Scores 12 to 20) are automated and executed on every Git commit:
1. `TC_RISK_01`: Unit test verifying that customer allergen set `avoid_allergens` strictly eliminates all intersecting candidates.
2. `TC_RISK_02`: Concurrency test attempting 11 bookings on a 10-capacity slot; verifying 11th order is rejected.
3. `TC_RISK_03`: Boundary test verifying candidate priced at ₹120.01 for a ₹100 base item is rejected ($> 20\%$).
4. `TC_RISK_04`: SQLite transaction verification ensuring `stock_qty` never drops below 0.
5. `TC_RISK_05`: Integration test verifying `orders` and `order_items` tables contain exact foreign key records.

---

## 5. Conclusion
Risk scoring identified that food safety (allergens) and slot overbooking constitute the highest business liability ($RES = 20$). Prioritizing these top 5 tests in CI/CD guarantees maximum defect mitigation with optimal test execution time.
