# Lab Experiment L2.4 — Sprint Velocity Data, Forecasting Model and Burndown Chart Analysis

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Framework:** Kanban / Scrum Hybrid  

---

## 1. Aim
To record team velocity across three past development sprints, formulate a statistical forecasting model to predict future release capacity, and analyze the ideal versus actual sprint burndown curve.

---

## 2. Historical Sprint Velocity Data

| Iteration | Committed Story Points | Completed Story Points | Completion Rate (%) | Primary Deliverables / Focus Area |
| :---: | :---: | :---: | :---: | :--- |
| **Sprint 1** | 20 | 18 | 90.0% | SQLite schema, catalog models, cart session state. |
| **Sprint 2** | 24 | 22 | 91.7% | Substitution ranking engine, allergen exclusion, PyTest suite. |
| **Sprint 3** | 22 | 20 | 90.9% | Delivery slot capacity logic, checkout UI, order confirmation. |
| **Total** | **66** | **60** | **90.9%** | **Baseline 3-Sprint Performance** |

### Statistical Velocity Metrics:
- **Average Team Velocity ($\bar{V}$):**
  $$\bar{V} = \frac{18 + 22 + 20}{3} = \frac{60}{3} = \mathbf{20.0\text{ Story Points / Sprint}}$$
- **Standard Deviation ($\sigma$):**
  $$\sigma = \sqrt{\frac{(18-20)^2 + (22-20)^2 + (20-20)^2}{3}} = \sqrt{\frac{4 + 4 + 0}{3}} = \sqrt{2.67} \approx \mathbf{1.63\text{ Points}}$$
- **Confidence Intervals for Future Sprint Planning:**
  - *Conservative Capacity (90% confidence):* $\bar{V} - \sigma = 20.0 - 1.63 = \mathbf{18.37\text{ points}}$
  - *Expected Capacity:* $\mathbf{20.0\text{ points}}$
  - *Optimistic Capacity:* $\bar{V} + \sigma = 20.0 + 1.63 = \mathbf{21.63\text{ points}}$

---

## 3. Backlog Forecasting Spreadsheet

Given remaining product backlog features totaling **38 Story Points** (mobile push alerts, dynamic slot pricing, multi-store pickup, customer reordering):

$$\text{Forecasted Sprints to Release} = \frac{\text{Remaining Backlog Points}}{\text{Average Velocity}} = \frac{38}{20} = \mathbf{1.90\text{ Sprints (approx. 2 Sprints)}}$$

---

## 4. Burndown Chart Analysis

The sprint burndown chart visualizes remaining work against time across a 10-day sprint cycle.

```
Story Points
25 | * (Day 1: 22 pts committed)
20 |   \  (Ideal linear slope: -2.2 pts/day)
15 |     *---* (Days 3-4: Flat plateau due to allergen edge case defect)
10 |          \
 5 |           *--* (Days 7-8: Swarm on Selenium test failures)
 0 +---------------------------------
   D1  D2  D3  D4  D5  D6  D7  D8  D9 D10 (Sprint Days)
```

- **Visual Evidence:** The actual burndown chart generated from sprint tracking is captured at [screenshots/burndown.png](file:///e:/Case37-Online-Grocery/screenshots/burndown.png).
- **Plateau Observation (Days 3–4):** Progress stalled when unit tests caught subtle case-sensitivity failures in candidate allergen matching. The pod swarmed to refactor `casefold()` set operations, after which burndown steepened back toward the ideal trajectory.
- **Sprint Completion:** Finished with 2 remaining points carried over to the next increment, achieving 91% sprint success.
