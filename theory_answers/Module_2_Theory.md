# Part 2: Theory Answers — Module 2: Agile Practices and AI-Driven Planning, Estimation and Scheduling

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Methodology:** Kanban | **AI Tool:** ChatGPT | **Module Focus:** Order Picking & Planning  

---

### T2.1: The Agile Manifesto and Principles Mapped to Online Grocery

The Agile Manifesto was drafted to move software engineering away from document-heavy, rigid planning toward responsive, human-centric software delivery.

#### 1. The Four Core Agile Values Applied to Online Grocery:

| Agile Manifesto Value | Traditional Waterfall Thinking | FreshCart Online Grocery Application (Case 37) |
| :--- | :--- | :--- |
| **Individuals and interactions over processes and tools** | Relying on strict hierarchical sign-off forms between pickers, stockers, and managers. | Store pickers and software developers interact directly in daily standups to refine mobile picking UI and substitution ergonomics. |
| **Working software over comprehensive documentation** | Writing a 200-page functional spec before writing a single line of database code. | Delivering a working **Substitution Logic Prototype** early that stakeholders can click, test, and approve with synthetic grocery orders. |
| **Customer collaboration over contract negotiation** | Freezing customer delivery terms and disallowing any changes once the order is placed. | The system actively collaborates with the customer during out-of-stock events, presenting clear options to **Accept** or **Reject** alternatives. |
| **Responding to change over following a plan** | Sticking to pre-set delivery schedules even when sudden supply chain disruptions occur. | The Kanban board dynamically adjusts WIP limits and delivery slot capacities when stock delays or weather events affect vehicle routing. |

#### 2. Key Agile Principles in Online Grocery Operations:
- **Early and Continuous Delivery:** Increment 1 delivers basic catalog ordering in week 1; Increment 2 adds intelligent substitution; Increment 3 adds capacity-constrained slot booking.
- **Welcoming Changing Requirements:** If store management introduces new dietary filters (e.g. plant-based vegan milk), the architecture easily accepts new tag-filtering rules without major refactoring.
- **Daily Collaboration:** Retail inventory personnel and development engineers review daily picking error logs to refine the algorithm.

---

### T2.2: The Kanban Framework, Roles, Core Practices, and Limitations

#### 1. Core Principles of Kanban:
Unlike Scrum (which organizes work into fixed time-boxed sprints), **Kanban is a continuous-flow Lean-Agile framework**. Kanban is founded on four foundational principles:
1. *Start with what you do now.*
2. *Agree to pursue evolutionary, incremental change.*
3. *Respect current roles, responsibilities, and job titles.*
4. *Encourage acts of leadership at all levels.*

#### 2. Six Core Practices of Kanban Applied to Case 37:
1. **Visualize the Workflow:** All order-picking engineering tasks are displayed on a physical or digital board across distinct lifecycle states (Backlog $\to$ Ready $\to$ In Progress $\to$ Review/Test $\to$ Done).
2. **Limit Work in Progress (WIP):** By capping *In Progress* at 3 and *Review/Test* at 2, developers are prevented from starting new tasks before finishing current ones, dramatically decreasing cycle time.
3. **Manage Flow:** Bottlenecks (such as code reviews for allergen logic) are made immediately visible as cards accumulate in front of WIP limits.
4. **Make Policies Explicit:** Clear transition criteria are posted (e.g., *A story cannot move to Done until PyTest coverage is $\ge 80\%$ and SonarQube reports zero blocker issues*).
5. **Implement Feedback Loops:** Daily stand-up cadences and replenishment meetings assess delivery slot fill rates and picking accuracy.
6. **Improve Collaboratively, Evolve Experimentally:** Use cumulative flow diagrams and lead-time metrics to systematically eliminate process wastes.

#### 3. Limitations of Kanban in Grocery Systems:
Kanban does not prescribe fixed delivery deadlines or milestone dates. For commercial retail grocery systems with hard marketing launches (e.g. Diwali festive grocery sale), Kanban must be supplemented with milestone-based release planning to guarantee delivery deadlines.

---

### T2.3: Agile Artifacts: Product Backlog, Sprint Backlog, Increment, and Definition of Done

```
+---------------------------------------------------------------------------------+
|                               Product Backlog                                   |
| (Prioritized master inventory of all features, enhancements, and defect fixes)  |
+---------------------------------------------------------------------------------+
          │
          ▼ (Sprint Planning / Replenishment)
+---------------------------------------------------------------------------------+
|                               Sprint Backlog                                    |
| (Committed work items for active development cycle: US-01, US-02, US-03)        |
+---------------------------------------------------------------------------------+
          │
          ▼ (Engineering, PyTest, Code Review, Dockerization)
+---------------------------------------------------------------------------------+
|                             Shippable Increment                                 |
| (Integrated, tested, deployable release meeting all Definition of Done criteria)|
+---------------------------------------------------------------------------------+
```

#### Detailed Definitions and Grocery Examples:

1. **Product Backlog:** The single source of truth containing all desired product capabilities. Example: User stories for slot capacity booking (US-01), real-time stock check (US-02), substitution engine (US-03), and mobile push alerts.
2. **Sprint Backlog / Kanban WIP:** The subset of product backlog items selected for active implementation. For Increment 2, the backlog focused strictly on the **Substitution Logic Prototype**.
3. **Increment:** The integrated sum of all completed backlog items during an iteration that is in a usable, shippable state. Example: FreshCart v1.0.0 container running on Docker with persistent SQLite database and responsive UI.
4. **Definition of Done (DoD):** The explicit, shared quality agreement that an item must satisfy before being considered complete:
   - [x] Code adheres to PEP 8 standards with zero SonarQube blockers.
   - [x] PyTest unit and integration tests written and passing ($100\%$ pass rate).
   - [x] Code coverage meets or exceeds the $80\%$ threshold (Current: $85\%$).
   - [x] Peer code review approved by at least one independent reviewer.
   - [x] Docker container builds cleanly and `/health` endpoint responds HTTP 200.
   - [x] User documentation and API schemas updated.

---

### T2.4: AI in Agile Estimation and Planning: Benefits, Hazards, and Reconciliation

#### 1. How AI Assists in Agile Estimation:
- **Story Decomposition:** ChatGPT rapidly breaks high-level epics (*"Order Fulfillment Engine"*) into granular user stories with acceptance criteria.
- **Baseline Complexity Sizing:** AI evaluates function signatures, database writes, and external dependencies to propose initial story points (e.g. 1, 2, 3, 5, 8).
- **Historical Velocity Forecasting:** Given past velocity figures (e.g. Sprint 1: 18 pts, Sprint 2: 22 pts, Sprint 3: 20 pts), AI calculates moving averages and generates burndown forecasts.

#### 2. The Hazards of Purely AI-Driven Estimation:
Large Language Models have no visceral understanding of real-world software engineering friction:
- AI does not account for environment setup delays, local Docker configuration issues, or flaky network dependencies.
- AI frequently underestimates concurrency hazards (e.g., race conditions when two customers simultaneously book the final delivery slot).
- AI assumes all required libraries install without conflict, which is rarely true in production environments.

#### 3. Human Reconciliation via Planning Poker:
In Case 37, team Planning Poker reconciled AI estimates:
- For **US-02 (Stock Concurrency Check)**, AI estimated **3 points**. The engineering team increased this to **5 points** because SQLite ACID transaction locking under multi-threaded browser sessions required custom retry mechanisms.

---

### T2.5: Agile Ceremonies and AI Collaboration

| Agile Ceremony | Traditional Activity | AI-Assisted Enhancement | Human Governance & Safeguard |
| :--- | :--- | :--- | :--- |
| **Sprint Planning / Replenishment** | Team discusses backlog items, debates scope, and estimates story points. | ChatGPT analyzes raw requirements and drafts Gherkin acceptance criteria. | **Team verifies feasibility:** Confirms whether slot booking rules match store logistics capacity. |
| **Daily Standup (15 min)** | Team answers: What did I do yesterday? What will I do today? What blocks me? | AI transcribes standup notes and flags recurring impediments across team members. | **Scrum Master removes blockers:** AI cannot fix a broken build or negotiate with suppliers. |
| **Sprint Review / Demo** | Team demonstrates working increment to store staff and customers. | AI auto-generates release notes and user-facing changelog from Git commits. | **Stakeholders click & test:** Store manager physically tests substitution flow on test device. |
| **Sprint Retrospective** | Team inspects its process: What went well? What didn't? Action items. | AI categorizes retrospective feedback into actionable themes (e.g., test delays). | **Team commits to action:** Engineers adopt new WIP limits and code review checklists. |
