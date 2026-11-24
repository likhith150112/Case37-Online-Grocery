# Lab Experiment L5.4 — Identification, Remediation, and Verification of a Deliberate AI Code Weakness

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Quality Assurance & Vulnerability Remediation  

---

## 1. Aim
To identify a subtle vulnerability in AI-generated code (acceptance of corrupt negative-priced catalog items), engineer a robust fix requiring strict positive price bounds, and execute an automated verification script proving that the vulnerability is neutralized.

---

## 2. Vulnerability Identification & Root Cause Analysis

### The Flawed AI Snippet:
```python
def flawed_ai_suggest_substitute(requested, candidates, max_price_increase=0.20):
    limit = requested.price * (1 + max_price_increase)
    valid = []
    for item in candidates:
        if item.category == requested.category and item.in_stock:
            if item.price <= limit:      # VULNERABILITY: -50.0 <= limit is True!
                valid.append(item)
    return valid[0]
```

### Root Cause:
The LLM checked only that candidate price was $\le limit$, naively assuming that all real-world retail prices are positive numbers. In database glitch scenarios (e.g., negative adjustment entries or promotional debit tokens with price $-₹10.00$), the flawed algorithm selected the negative item as the top substitute, causing severe accounting errors and billing corruption.

---

## 3. Engineering Remediation Applied

In `Module-5-Quality-Assurance/L5.4/weakness_fix.py`:
1. **Added Type and Value Guard:**
   ```python
   if not isinstance(requested, Product):
       raise TypeError("requested must be a Product instance")
   if requested.price <= 0:
       raise ValueError("requested price must be positive")
   ```
2. **Added Positive Price Filter:**
   ```python
   if item.price <= 0:
       continue  # Strictly eliminate zero and negative glitch prices
   ```

---

## 4. Execution Evidence & Verification

Executing `python Module-5-Quality-Assurance/L5.4/weakness_fix.py`:
```text
=== L5.4 Deliberate AI Weakness Discovery & Verification ===

[Step 1] Testing Flawed AI Code:
Flawed AI chose: Corrupt Glitch Item at ₹-10.0
--> CRITICAL VULNERABILITY CONFIRMED: Negative price item was selected as valid substitute!

[Step 2] Testing Fixed Human Engineering Code:
Fixed Code chose: Fresh Milk Alternate at ₹54.0
--> VERIFICATION PASSED: Glitch item successfully rejected. Legitimate product selected.
```

---

## 5. Conclusion
AI-generated code frequently misses negative-space edge cases. Enforcing strict positive boundary checks (`item.price > 0`) eliminated the flaw, protecting the store against corrupt financial transactions.
