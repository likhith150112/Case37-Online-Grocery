# Lab Experiment L1.5 — AI-Generated Test Cases, Gap Analysis and Accuracy Calculation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** Requirements & Testing | **AI Tool:** ChatGPT  

---

## 1. Aim
To generate a comprehensive test suite for the Substitution Logic module using ChatGPT, analyze gaps where AI missed critical boundary or negative test cases, and calculate the quantitative accuracy score of AI test generation.

---

## 2. Test Case Generation Prompt and AI Output

### The Prompt Given to ChatGPT:
```
Context: Python grocery substitution engine `suggest_substitution(requested, catalog, ...)`.
Generate 10 unit test cases covering nominal, boundary, and negative scenarios.
Include test description, inputs, expected outputs, and assertion types.
```

### AI-Generated Test Proposals:
1. `TC_AI_01`: Request item in stock $\to$ returns original item. (Valid - Nominal)
2. `TC_AI_02`: Item out of stock $\to$ suggests candidate in same category. (Valid - Nominal)
3. `TC_AI_03`: Different category item $\to$ excluded. (Valid - Negative)
4. `TC_AI_04`: Candidate price higher than $20\%$ $\to$ excluded. (Valid - Boundary)
5. `TC_AI_05`: Candidate price lower than original $\to$ accepted. (Valid - Nominal)
6. `TC_AI_06`: Empty catalog $\to$ returns None. (Valid - Negative)
7. `TC_AI_07`: Candidate contains customer allergen $\to$ excluded. (Valid - Negative)
8. `TC_AI_08`: Fast search check $\to$ response in $< 1\text{ second}$. (Invalid - Performance test, not unit testable without network harness)
9. `TC_AI_09`: Candidate price is negative (e.g. -₹10) $\to$ rejected. (Valid - Negative)
10. `TC_AI_10`: Customer accepts suggestion $\to$ database order placed. (Invalid - Overreaches unit scope into full integration/DB layer)

---

## 3. Human Gap Analysis: Critical Boundary & Negative Cases Missed by AI

Human engineering review revealed that while ChatGPT generated basic nominal and boundary tests, it overlooked 3 safety-critical edge cases:
1. **Missed Case 1 (Case-Insensitive Category Normalization):** AI assumed categories were always formatted identically. If requested had `"dairy"` and candidate had `"Dairy"`, naive string equality failed.
2. **Missed Case 2 (Type Safety on Requested Object):** AI forgot to test passing an invalid data type (e.g. passing a string `"MILK"` instead of a `Product` dataclass instance).
3. **Missed Case 3 (Negative Price Limit Argument):** AI forgot to test passing `max_price_increase = -5.0`, which should immediately raise a `ValueError`.

These 3 missing cases were engineered and added to our master PyTest suite (`test_08`, `test_09`, `test_10`).

---

## 4. Quantitative AI Accuracy Calculation

$$\text{Accuracy Rate} = \frac{\text{Valid, Directly Usable Test Cases}}{\text{Total Suggested Test Cases}} \times 100\%$$

$$\text{Defect Discovery Efficiency} = \frac{\text{Boundary / Negative Tests Generated}}{\text{Total Valid Tests}} \times 100\%$$

- Total Test Cases Suggested by AI: **10**
- Valid, Directly Usable Unit Test Cases: **8** (TC_AI_01 through TC_AI_07, and TC_AI_09)
- Flawed / Out-of-Scope Test Cases: **2** (TC_AI_08 conflated performance SLA; TC_AI_10 conflated DB integration)
- **AI Test Generation Accuracy:**
  $$\text{Accuracy} = \frac{8}{10} \times 100\% = \mathbf{80.0\%}$$
- Number of Boundary / Negative Tests among Valid Tests: **5 / 8** $\implies \mathbf{62.5\%}$

---

## 5. Conclusion
ChatGPT achieved an **80.0% accuracy rate** for unit test generation, providing a solid initial test scaffold. However, the human tester's gap analysis was critical to uncover missing type-validation checks and negative threshold constraints that are essential for robust e-commerce software.
