# Master Assignment Checklist — Case 37: Online Grocery

**Student Details:**
- **Name:** Likhith Gowda M S
- **Roll Number:** 37
- **USN:** ENG24CS0105
- **Section:** 5B
- **University:** Dayananda Sagar University, Bengaluru
- **Subject:** AI in Software Engineering
- **Case Number:** 37
- **Project Domain:** Online Grocery
- **Process Model:** Incremental
- **Agile Methodology:** Kanban
- **Required AI Tool:** ChatGPT
- **Prototype Module:** Substitution Logic

---

## Final Verification Summary Status

| Deliverable Group | Total Items | Completed | Executed / Verified | Evidence Attached |
| :--- | :---: | :---: | :---: | :---: |
| **Part 1: Case Tasks (A–E)** | 5 | 5 | **YES (100%)** | **YES** |
| **Part 2: Theory Questions (T1.1–T5.5)** | 25 | 25 | **YES (100%)** | **YES** |
| **Part 3: Lab Experiments (L1.1–L5.5)** | 25 | 25 | **YES (100%)** | **YES** |
| **Total Assignment Deliverables** | **55** | **55** | **YES (100%)** | **YES** |

---

## Detailed Master Tracking Table

### Part 1: Case Tasks (5 Tasks)

| Item ID | Description | Target Path | Status | Evidence File / Artifact |
| :--- | :--- | :--- | :---: | :--- |
| **Task A** | Incremental lifecycle & AI-assisted requirements from store-staff chat | `case_tasks/Task_A_Incremental_Lifecycle.md` | **COMPLETED** | `screenshots/incremental_sdlc.png` |
| **Task B** | Kanban board with WIP limits for order-picking features & AI estimation | `case_tasks/Task_B_Kanban_Order_Picking.md` | **COMPLETED** | `screenshots/kanban.png`, `burndown.png` |
| **Task C** | Copilot-assisted substitution rules, Git, Jenkins and Docker | `case_tasks/Task_C_Substitution_Logic_DevOps.md` | **COMPLETED** | `Dockerfile`, `Jenkinsfile`, git history |
| **Task D** | Selenium order flow, AI-generated test data & defect prediction | `case_tasks/Task_D_Testing_Defect_Prediction.md` | **COMPLETED** | `tests/test_selenium_order_flow.py`, defect model |
| **Task E** | Usability, SonarQube & ethics of AI-driven price personalisation | `case_tasks/Task_E_Quality_Ethics_Pricing.md` | **COMPLETED** | `sonar-project.properties`, audit logs |

---

### Part 2: Theory Questions (25 Questions)

| ID | Module | Question Description | Path | Status | Verification Detail |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **T1.1** | SDLC | Software engineering & SDLC: disciplined engineering approach for grocery | `theory_answers/Module_1_Theory.md` | **COMPLETED** | 7 SDLC phases, grocery rationale |
| **T1.2** | SDLC | Process model evaluation & ranking (Incremental, Agile, Spiral, V-Model, Waterfall) | `theory_answers/Module_1_Theory.md` | **COMPLETED** | Weighted matrix, Incremental #1 |
| **T1.3** | SDLC | AI-driven lifecycle vs traditional SDLC across phases with human checkpoints | `theory_answers/Module_1_Theory.md` | **COMPLETED** | Phase-by-phase comparison table |
| **T1.4** | SDLC | AI-enabled tools (Copilot, Tabnine, ChatGPT) evaluation & data protection | `theory_answers/Module_1_Theory.md` | **COMPLETED** | Tool matrix & zero-PII policy |
| **T1.5** | SDLC | Limits of AI-assisted requirements & engineering resolution techniques | `theory_answers/Module_1_Theory.md` | **COMPLETED** | Disambiguation & Gherkin rules |
| **T2.1** | Agile | Agile values and principles mapped to Online Grocery operations | `theory_answers/Module_2_Theory.md` | **COMPLETED** | 4 values & 12 principles mapped |
| **T2.2** | Agile | Kanban framework, core practices, grocery board WIP limits & limitations | `theory_answers/Module_2_Theory.md` | **COMPLETED** | WIP limits: In Progress=3, Review=2 |
| **T2.3** | Agile | Scrum/Agile artifacts: Product Backlog, Sprint Backlog, Increment, and DoD | `theory_answers/Module_2_Theory.md` | **COMPLETED** | Grocery examples & 6-point DoD |
| **T2.4** | Agile | AI-assisted user story generation, point estimation & human reconciliation | `theory_answers/Module_2_Theory.md` | **COMPLETED** | Planning poker vs AI analysis |
| **T2.5** | Agile | Agile ceremonies, team collaboration, and AI benefits/risks in sprint tracking | `theory_answers/Module_2_Theory.md` | **COMPLETED** | 4 ceremonies & AI governance |
| **T3.1** | Dev/DevOps | Role prompting, few-shot prompting, and chain-of-thought prompt engineering | `theory_answers/Module_3_Theory.md` | **COMPLETED** | Comparative evaluation scorecard |
| **T3.2** | Dev/DevOps | AI-assisted coding risks: security vulnerabilities, hallucinations & licensing | `theory_answers/Module_3_Theory.md` | **COMPLETED** | SQLi, secrets, negative price fix |
| **T3.3** | Dev/DevOps | Git branching strategy (trunk/feature branching), pull requests & merge conflicts | `theory_answers/Module_3_Theory.md` | **COMPLETED** | Gitflow & PR governance checklist |
| **T3.4** | Dev/DevOps | Continuous Integration with Jenkins: automated build triggers & pipeline stages | `theory_answers/Module_3_Theory.md` | **COMPLETED** | 6 pipeline stages in Jenkinsfile |
| **T3.5** | Dev/DevOps | Docker containerization fundamentals: Dockerfile, images, containers & portability | `theory_answers/Module_3_Theory.md` | **COMPLETED** | VM vs Container & line-by-line |
| **T4.1** | Testing | Levels of testing (Unit, Integration, System, Acceptance) in grocery application | `theory_answers/Module_4_Theory.md` | **COMPLETED** | Testing pyramid & grocery mapping |
| **T4.2** | Testing | Black-box vs white-box test design techniques applied to substitution logic | `theory_answers/Module_4_Theory.md` | **COMPLETED** | EP, BVA, Decision tables, Coverage |
| **T4.3** | Testing | Automated testing vs manual testing: trade-offs, break-even analysis & regression | `theory_answers/Module_4_Theory.md` | **COMPLETED** | Break-even math ($N \approx 2.69$ cycles) |
| **T4.4** | Testing | AI in test case generation, synthetic test data privacy & edge case discovery | `theory_answers/Module_4_Theory.md` | **COMPLETED** | Privacy safeguards, synthetic personas |
| **T4.5** | Testing | Continuous health monitoring, synthetic probes, response time thresholds & alerts | `theory_answers/Module_4_Theory.md` | **COMPLETED** | `/health` probe & 2.0s alert logic |
| **T5.1** | QA & Ethics | Software quality attributes (ISO 25010), defect density, and failure rate metrics | `theory_answers/Module_5_Theory.md` | **COMPLETED** | ISO 25010 8 characteristics & math |
| **T5.2** | QA & Ethics | Static code analysis, SonarQube quality gates, code smells & security hotspots | `theory_answers/Module_5_Theory.md` | **COMPLETED** | Bugs, smells, hotspots, quality gates |
| **T5.3** | QA & Ethics | AI code review vs human peer review: strengths, blind spots & checklists | `theory_answers/Module_5_Theory.md` | **COMPLETED** | Two-tier review policy |
| **T5.4** | QA & Ethics | Software reliability engineering, MTBF/MTTR, and defect prediction models | `theory_answers/Module_5_Theory.md` | **COMPLETED** | Availability formula & logistic model |
| **T5.5** | QA & Ethics | Ethical AI development: demographic fairness, pricing transparency & privacy | `theory_answers/Module_5_Theory.md` | **COMPLETED** | Feature blinding & demographic parity |

---

### Part 3: Lab Experiments (25 Experiments)

| ID | Module | Experiment Title & Objective | Folder | Status | Evidence File / Output |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **L1.1** | M1 | One-page SDLC plan with phase breakdown & Incremental delivery | `Module-1-SDLC/L1.1` | **COMPLETED** | `plan.md`, `incremental_sdlc.png` |
| **L1.2** | M1 | Weighted decision matrix (5 models × 5 criteria) & justification | `Module-1-SDLC/L1.2` | **COMPLETED** | `README.md`, weighted score 9.25 |
| **L1.3** | M1 | Manual vs AI-assisted substitution code with change log | `Module-1-SDLC/L1.3` | **COMPLETED** | `manual_substitution.py`, `ai_substitution.py` |
| **L1.4** | M1 | 10 FRs and 5 NFRs with before/after testable acceptance criteria | `Module-1-SDLC/L1.4` | **COMPLETED** | `README.md` (FR-01 to FR-10, NFR-01 to NFR-05) |
| **L1.5** | M1 | AI test generation, boundary/negative cases & accuracy calculation | `Module-1-SDLC/L1.5` | **COMPLETED** | `README.md` (Accuracy = 80.0%) |
| **L2.1** | M2 | Agile working agreement for online grocery engineering team | `Module-2-Agile/L2.1` | **COMPLETED** | `README.md` (Communication, SLAs, DoD) |
| **L2.2** | M2 | Kanban framework, roles, board setup, WIP limits & policies | `Module-2-Agile/L2.2` | **COMPLETED** | `README.md`, `screenshots/kanban.png` |
| **L2.3** | M2 | One epic, 5 user stories (US-01 to US-05) & acceptance criteria | `Module-2-Agile/L2.3` | **COMPLETED** | `README.md` (5 Gherkin user stories) |
| **L2.4** | M2 | Sprint velocity data, forecasting spreadsheet & burndown chart | `Module-2-Agile/L2.4` | **COMPLETED** | `README.md`, `screenshots/burndown.png` |
| **L2.5** | M2 | 10 tickets, AI summarisation, duplicate detection & accuracy | `Module-2-Agile/L2.5` | **COMPLETED** | `README.md` (Accuracy = 66.7% / 100%) |
| **L3.1** | M3 | Role prompting, few-shot prompting & step-by-step prompt evaluation | `Module-3-Development/L3.1` | **COMPLETED** | `README.md` (CoT Score: 9.63 / 10) |
| **L3.2** | M3 | Working substitution prototype with accepted/rejected AI suggestion log | `Module-3-Development/L3.2` | **COMPLETED** | `README.md` (5 audit decisions logged) |
| **L3.3** | M3 | GitHub branch protection rules & blocked PR until review passes | `Module-3-Development/L3.3` | **COMPLETED** | `README.md` (Branch protection walkthrough) |
| **L3.4** | M3 | Jenkins pipeline configuration with push trigger & 2 build results | `Module-3-Development/L3.4` | **COMPLETED** | `Jenkinsfile`, Build #1 fail, Build #2 pass |
| **L3.5** | M3 | Dockerfile line-by-line explanation, image build & container run | `Module-3-Development/L3.5` | **COMPLETED** | `Dockerfile`, container terminal commands |
| **L4.1** | M4 | 20-minute exploratory testing session notes & discovered issues | `Module-4-Testing/L4.1` | **COMPLETED** | `README.md` (Session charter & bug notes) |
| **L4.2** | M4 | 8 PyTest unit tests with actual coverage report (>=80%) | `Module-4-Testing/L4.2` | **COMPLETED** | `execution_logs/pytest_execution_log.txt` (85%) |
| **L4.3** | M4 | 10 test cases manual vs Selenium, 5 repetitions, break-even math | `Module-4-Testing/L4.3` | **COMPLETED** | `README.md` ($N = 2.69 \approx 3$ cycles) |
| **L4.4** | M4 | Risk scoring for 10 test cases (likelihood × impact), top 5 selection | `Module-4-Testing/L4.4` | **COMPLETED** | `README.md` (Top 5 P1/P2 tests prioritized) |
| **L4.5** | M4 | 10-minute monitoring script checking /health, response logs & chart | `Module-4-Testing/L4.5` | **COMPLETED** | `monitor.py`, `execution_logs/monitor.log` |
| **L5.1** | M5 | Defect density & reliability measurement over 50 actual runs | `Module-5-Quality-Assurance/L5.1` | **COMPLETED** | `reliability_test.py` (100% success, $D=2.43$) |
| **L5.2** | M5 | SonarQube analysis, fixing 5 genuine issues, rescan before/after | `Module-5-Quality-Assurance/L5.2` | **COMPLETED** | `README.md` (0 bugs, 0 smells, 85% coverage) |
| **L5.3** | M5 | AI code-review checklist applied to real AI substitution suggestion | `Module-5-Quality-Assurance/L5.3` | **COMPLETED** | `README.md` (7-point checklist signed off) |
| **L5.4** | M5 | Identification & fix of deliberate weakness in AI code with unit test | `Module-5-Quality-Assurance/L5.4` | **COMPLETED** | `weakness_fix.py` (Negative price fix tested) |
| **L5.5** | M5 | AI fairness & bias testing across names, regions, genders with audit | `Module-5-Quality-Assurance/L5.5` | **COMPLETED** | `README.md` (100% demographic parity verified) |

---
