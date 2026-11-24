# Lab Experiment L5.5 — AI Fairness Testing Across Demographic Personas and Mitigation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** AI Ethics, Fairness & Algorithmic Bias Mitigation  

---

## 1. Aim
To execute systematic algorithmic fairness testing on the FreshCart recommendation and pricing engine across synthetic demographic personas (varying names, gender identities, and geographic regions), verify demographic parity, and establish architectural safeguards against bias.

---

## 2. Fairness Testing Methodology (Synthetic Profiles Only)
In accordance with ethical data guidelines, zero real customer information was used. Five synthetic profiles were created where the ordered grocery basket (`MIL-002: Amul Taaza Milk 1L`, base price ₹54.00, out-of-stock) was held strictly constant, while demographic attributes varied:

| Persona ID | Synthetic Name | Gender Indicator | Regional Zone | Dietary Profile | Target Item Evaluated |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **PER-01** | Likhith Gowda | Male | South Bengaluru | Standard | MIL-002 (Amul Milk) |
| **PER-02** | Aarav Sharma | Male | North Bengaluru | Standard | MIL-002 (Amul Milk) |
| **PER-03** | Ananya Iyer | Female | South Bengaluru | Standard | MIL-002 (Amul Milk) |
| **PER-04** | Priya Nair | Female | East Bengaluru | Standard | MIL-002 (Amul Milk) |
| **PER-05** | Mohammed Zaid | Male | Central Bengaluru | Standard | MIL-002 (Amul Milk) |

---

## 3. Empirical Execution Results

Each persona executed the substitution evaluation through `grocery_app/substitution.py`.

```text
Evaluating Fairness Test Runs:
PER-01 (Likhith Gowda - Male - South):   Suggested: MIL-001 (Nandini Milk) | Price: ₹44.00 | Delta: -₹10.00
PER-02 (Aarav Sharma - Male - North):    Suggested: MIL-001 (Nandini Milk) | Price: ₹44.00 | Delta: -₹10.00
PER-03 (Ananya Iyer - Female - South):   Suggested: MIL-001 (Nandini Milk) | Price: ₹44.00 | Delta: -₹10.00
PER-04 (Priya Nair - Female - East):     Suggested: MIL-001 (Nandini Milk) | Price: ₹44.00 | Delta: -₹10.00
PER-05 (Mohammed Zaid - Male - Central): Suggested: MIL-001 (Nandini Milk) | Price: ₹44.00 | Delta: -₹10.00
```

### Fairness Evaluation Metrics:
- **Demographic Parity Ratio:** $1.00$ ($100\%$ parity across all 5 demographic variations).
- **Price Disparity:** $₹0.00$ variance across demographic groups.
- **Candidate Ranking Parity:** $100\%$ identical ranking order (`MIL-001` ranked #1 for every user).

---

## 4. Architectural Mitigation Safeguards

1. **Feature Blinding:** The `Product` and `Substitution` dataclasses and the algorithm `suggest_substitution` do not accept customer demographic fields (name, gender, ethnicity, address) as inputs. The algorithm operates strictly on objective attributes: category, price, inventory count, and dietary tags.
2. **Deterministic Tie-Breaking:** If two candidates have identical price deltas, tie-breaking is based on alphabetical product name (`item.name.casefold()`), ensuring repeatable, unbiased selection.
3. **Price Invariance Guarantee:** FreshCart enforces that essential food prices are identical for all customers, prohibiting dynamic AI price inflation based on device or customer profile.

---

## 5. Conclusion
Fairness testing proved that the FreshCart Substitution Logic treats all customers with complete demographic parity. Algorithmic blinding prevents bias from entering essential grocery fulfillment.
