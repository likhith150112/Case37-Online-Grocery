# Lab Experiment L1.2 — Weighted Decision Matrix for Process Model Selection

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  

---

## 1. Aim
To mathematically evaluate and justify the selection of the **Incremental Model** over four competing SDLC models (Waterfall, V-Model, Spiral, and Agile/Scrum) using a 5-criteria weighted decision matrix.

## 2. Evaluation Criteria and Weightage
1. **Requirements Flexibility (Weight: 0.25):** Ability to adapt when supermarket stock levels, brand partnerships, or delivery slot policies change.
2. **Early Business Delivery (Weight: 0.25):** Speed of delivering a functional, usable catalog to generate early customer revenue and gather real shopping feedback.
3. **Risk Management & Safety (Weight: 0.20):** Ability to isolate and test high-risk modules (allergen filtering and price ceiling algorithms).
4. **Architectural Discipline (Weight: 0.15):** Maintaining consistent database schemas, primary keys, and transaction integrity.
5. **Team Resource Efficiency (Weight: 0.15):** Feasibility of execution by an engineering student pod without enterprise process bloat.

## 3. Weighted Decision Matrix Calculation

$$\text{Weighted Score} = \sum_{i=1}^{5} (\text{Weight}_i \times \text{Raw Score}_i) \quad \text{where Raw Score} \in [1, 10]$$

| Evaluation Criteria | Weight ($W_i$) | Incremental Model | Agile (Scrum/Kanban) | Spiral Model | V-Model | Waterfall Model |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Requirements Flexibility | 0.25 | 9.0 (2.25) | 10.0 (2.50) | 8.0 (2.00) | 5.0 (1.25) | 3.0 (0.75) |
| Early Business Delivery | 0.25 | 10.0 (2.50) | 9.0 (2.25) | 6.0 (1.50) | 4.0 (1.00) | 2.0 (0.50) |
| Risk Management & Safety | 0.20 | 9.0 (1.80) | 8.0 (1.60) | 10.0 (2.00) | 8.0 (1.60) | 5.0 (1.00) |
| Architectural Discipline| 0.15 | 9.0 (1.35) | 7.0 (1.05) | 8.0 (1.20) | 10.0 (1.50) | 9.0 (1.35) |
| Team Resource Efficiency| 0.15 | 9.0 (1.35) | 9.0 (1.35) | 5.0 (0.75) | 6.0 (0.90) | 7.0 (1.05) |
| **Total Weighted Score** | **1.00** | **9.25** | **8.75** | **7.45** | **6.25** | **4.65** |
| **Final Ranking** | — | **Rank 1 (Selected)** | **Rank 2** | **Rank 3** | **Rank 4** | **Rank 5** |

## 4. Five-Line Conclusion Supporting the Incremental Model
1. The **Incremental Model scored highest (9.25 / 10)** because it directly balances early working software with disciplined architectural stability.
2. Delivering the basic catalog in Increment 1 allows immediate customer shopping while isolating the **Substitution Logic prototype** into Increment 2.
3. This staged approach eliminates the all-or-nothing delivery risk inherent in the Waterfall and V-Models.
4. Furthermore, it avoids the process overhead and excessive risk analysis cycles of the Spiral Model that overburden a student engineering pod.
5. Consequently, the Incremental Model is the optimal software engineering methodology for Case 37 (Online Grocery).
