# Lab Experiment L2.1 — Agile Team Working Agreement

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Framework:** Kanban | **Team Size:** 4 Engineering Students  

---

## 1. Aim
To establish a formal, collaborative Agile Working Agreement defining team norms, communication channels, core working hours, code review service-level agreements (SLAs), and explicit quality standards for the FreshCart engineering pod.

---

## 2. Core Pillars of the Working Agreement

### 1. Communication Cadence & Channels
- **Primary Async Channel:** Microsoft Teams / Discord engineering channel `#case37-online-grocery`.
- **Daily Standup:** 15 minutes daily at 09:30 AM IST (In-person or virtual). Structure:
  1. *What did you complete since yesterday?*
  2. *What will you finish today?*
  3. *What blockers or technical impediments are halting your flow?*
- **Emergency Escalation:** If a build breaks on `master`, ping Project Lead directly; pod swarms immediately to restore green status.

### 2. Work-in-Progress (WIP) and Pull Request Policies
- **Strict Adherence to WIP Limits:** No developer shall pull a new ticket from *Ready* if *In Progress* already holds 3 active items.
- **Pull Request Review SLA:** Every PR must be reviewed and feedback provided within **4 hours** of submission.
- **Independent Peer Approval:** At least one peer review approval is required prior to merging; no self-merging permitted.

### 3. Code Standards & Quality Benchmarks
- All Python code must strictly follow **PEP 8** style guidelines.
- Functions must have descriptive docstrings and static type annotations (`typing`).
- Every new feature must include corresponding PyTest tests; overall repository coverage must remain $\ge 80\%$.
- SonarQube static scan must report **Zero Blocker and Zero Critical issues**.

### 4. Definition of Done (DoD) Checklist
A user story or engineering task is marked **Done** only when:
- [x] Code implemented and pushed to feature branch.
- [x] PyTest unit and integration tests passing ($100\%$ pass rate).
- [x] Test coverage verified $\ge 80\%$.
- [x] Code review completed and approved on GitHub PR.
- [x] Docker image builds cleanly and passes `/health` probe.
- [x] Documentation updated in master checklist and README.

---

## 3. Team Sign-Off and Commitment

| Team Role | Name | USN | Signature Status |
| :--- | :--- | :--- | :---: |
| **Project Lead & Backend** | Likhith Gowda M S | ENG24CS0105 | **Committed / Signed** |
| **Frontend Engineer** | Peer Student 1 | ENG24CS0106 | **Committed / Signed** |
| **QA / Automation Lead** | Peer Student 2 | ENG24CS0107 | **Committed / Signed** |
| **DevOps & Release Lead** | Peer Student 3 | ENG24CS0108 | **Committed / Signed** |
