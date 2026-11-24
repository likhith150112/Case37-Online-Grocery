# Lab Experiment L3.1 — Prompt Engineering: Comparative Evaluation of Role, Few-Shot, and Step-by-Step Prompting

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Development Practices | **AI Tool:** ChatGPT  

---

## 1. Aim
To execute, evaluate, and compare three distinct prompt engineering paradigms (Role Prompting, Few-Shot Prompting, and Step-by-Step / Chain-of-Thought Prompting) for generating the core `suggest_substitution` algorithm, measuring output correctness, safety, and readability.

---

## 2. Experimental Execution

### Paradigm 1: Role Prompting
- **Prompt:** *"Act as a Senior Python Architect specializing in Retail E-Commerce and Inventory Systems. Using Python dataclasses and PEP 8 static type hints, write a function `suggest_substitution` that recommends replacements for unavailable items."*
- **Observed Output Quality:** Clean, modular structure using `@dataclass(frozen=True)`. Produced strong type annotations. However, omitted negative price threshold validations (`max_price_increase < 0`).

### Paradigm 2: Few-Shot Prompting
- **Prompt:** Provide 3 concrete input/output demonstrations:
  - *Example 1:* Requested item is in-stock $\to$ Return requested item directly.
  - *Example 2:* Requested `MIL-001` (Dairy, ₹50, out) $\to$ Candidate `MIL-002` (Dairy, ₹55, in) accepted; Candidate `OIL-001` (Oil) rejected.
  - *Example 3:* Customer avoids `tree-nut` $\to$ Candidate `MIL-004` (Almond Milk, contains `tree-nut`) excluded.
- **Observed Output Quality:** Strong adherence to allergen exclusion and category matching. However, sorting logic was simplistic (picked the first passing candidate rather than ranking by price proximity).

### Paradigm 3: Step-by-Step (Chain-of-Thought) Prompting
- **Prompt:** *"Think step by step to build `suggest_substitution`:
  1. Validate requested item type and non-negative parameters.
  2. If requested is in stock, return it with zero delta.
  3. Normalize customer allergens to lowercase sets.
  4. Filter candidates: category match, in stock, positive price, no allergens, price delta <= max limit.
  5. Rank candidates by matching customer preferred tags, then lowest price delta.
  6. Return structured Substitution object."*
- **Observed Output Quality:** **Flawless algorithmic logic.** Successfully handled all boundary cases, type errors, and deterministic tie-breaking.

---

## 3. Comparative Metric Scorecard

| Evaluation Dimension | Weight | Role Prompting | Few-Shot Prompting | Step-by-Step (CoT) Prompting |
| :--- | :---: | :---: | :---: | :---: |
| **Syntactic & Architectural Quality** | 0.25 | 9.5 / 10 | 8.0 / 10 | **9.5 / 10** |
| **Edge-Case & Boundary Handling** | 0.25 | 6.5 / 10 | 8.5 / 10 | **10.0 / 10** |
| **Allergen & Dietary Safety** | 0.25 | 6.0 / 10 | 9.5 / 10 | **10.0 / 10** |
| **Code Readability & Maintainability** | 0.25 | 9.0 / 10 | 7.5 / 10 | **9.0 / 10** |
| **Composite Score** | **1.00** | **7.75 / 10** | **8.38 / 10** | **9.63 / 10 (Selected)** |

---

## 4. Conclusion
Step-by-step (Chain-of-Thought) prompting achieved the highest score (**9.63 / 10**), eliminating logical skips and producing production-ready code with complete safety validation. The resulting code was adopted as the foundation for `grocery_app/substitution.py`.
