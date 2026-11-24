# Case Task B — Kanban Board with WIP Limits and AI Effort Estimation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Framework:** Kanban | **AI Tool:** ChatGPT  

---

## 1. Kanban Framework and Board Structure

In a fast-paced retail environment like Online Grocery fulfillment, work arrives continuously (orders placed every minute) rather than in fixed two-week batch increments. Therefore, **Kanban** was selected as the optimal Lean-Agile framework.

Kanban optimizes the **flow of work**, visualizes bottlenecks in order picking and substitution, and enforces strict **Work-in-Progress (WIP) limits** to prevent inventory stock desynchronization.

### 1.1 FreshCart Kanban Workflow Columns and WIP Limits

```
+----------------+----------------+----------------+----------------+----------------+
|    Backlog     |     Ready      |  In Progress   |  Review / Test |      Done      |
|  (WIP: None)   |    (WIP: 5)    |    (WIP: 3)    |    (WIP: 2)    |  (WIP: None)   |
+----------------+----------------+----------------+----------------+----------------+
| - Real-time    | - Auto-sync    | - Rule-based   | - Allergen     | - Customer     |
|   push alerts  |   inventory    |   item ranking |   filter test  |   slot booking |
| - Dynamic price| - Slot expiry  | - Order-pick   | - Slot lock    | - SQLite schema|
|   delta calc   |   timer        |   route UI     |   verification |   init         |
+----------------+----------------+----------------+----------------+----------------+
```

### 1.2 Justification for Specific WIP Limits
- **In Progress (WIP = 3):** With a 3-engineer development pod, capping active engineering tasks at 3 guarantees that developers do not multitask. If a developer faces a blocking database lock or algorithm hurdle, the entire pod swarms to resolve it rather than pulling new stories.
- **Review / Test (WIP = 2):** In safety-critical modules like allergen filtering and price variance verification, code review cannot be rushed. Capping Review at 2 prevents pull requests from piling up and decaying.

---

## 2. Order-Picking Feature Work Items and User Stories

| Work Item ID | Feature Title | Priority | AI Story Point | Team Planning Poker | Variance Analysis & Reconciliation | Acceptance Criteria |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **US-01** | Delivery Slot Selection | High | 3 | 3 | **Agreed (0 delta):** Standard UI form radio buttons and capacity query. | Only slots where $(Capacity - Booked) > 0$ can be selected; full slots show disabled red badge. |
| **US-02** | Real-Time Stock Validation | High | 3 | 5 | **AI underestimated (-2):** AI overlooked race conditions when 2 users checkout the last milk packet simultaneously. Team added 2 points for SQLite transactions. | Stock check executes within ACID transaction prior to checkout; raises out-of-stock warning. |
| **US-03** | Suggest Intelligent Substitute | High | 5 | 5 | **Agreed (0 delta):** Dataclass-based ranking algorithm with price caps and category matching. | Proposes top in-stock candidate in identical category where $\Delta \text{Price} \le 20\%$. |
| **US-04** | Customer Approval Workflow | High | 2 | 3 | **AI underestimated (-1):** AI considered only the UI button; team added points for cart SKU swapping and audit logging. | Customer can accept (swaps SKU) or reject (removes item); decision saved in `order_items`. |
| **US-05** | Order Confirmation & Health API | Medium | 2 | 3 | **AI underestimated (-1):** AI missed database health connectivity check inside the health endpoint. | `/health` returns HTTP 200 with JSON payload (`healthy`, `database: UP`, `items`, `timestamp`). |

---

## 3. Planning Poker vs. AI Estimation Analysis

To evaluate AI accuracy in agile estimation, each user story was estimated independently by ChatGPT and by a 4-student student engineering team using Fibonacci planning poker cards (1, 2, 3, 5, 8, 13).

```
Comparative Story Point Estimation Chart:
US-01 [Slot Selection]:      AI = 3 | Team = 3  [Match]
US-02 [Stock Check]:         AI = 3 | Team = 5  [Team higher due to concurrency & race condition handling]
US-03 [Substitution Logic]:  AI = 5 | Team = 5  [Match]
US-04 [Approval Workflow]:   AI = 2 | Team = 3  [Team higher due to cart state reconciliation & UI alerts]
US-05 [Health & Confirm]:    AI = 2 | Team = 3  [Team higher due to JSON schema & DB probe requirements]
```

### Key Finding on AI Estimation in Agile:
ChatGPT tends to estimate based solely on **syntactic code complexity** (lines of code, loops, data structures). Human engineering teams correctly identify **system integration risks**, concurrency hazards, and edge cases that inflate actual implementation effort. AI estimates serve as an excellent baseline starting point, but human team reconciliation is indispensable.

---

## 4. Kanban Artifacts & Visual Evidence

- **Kanban Board Visualization:** The complete board with story swimlanes, WIP constraints, and task progression is documented at [screenshots/kanban.png](file:///e:/Case37-Online-Grocery/screenshots/kanban.png).
- **Sprint / Cumulative Flow Burndown:** The ideal vs actual burndown tracking delivery progress across increments is documented at [screenshots/burndown.png](file:///e:/Case37-Online-Grocery/screenshots/burndown.png).
