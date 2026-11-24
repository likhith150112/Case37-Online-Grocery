# Lab Experiment L1.1 — One-Page SDLC Plan

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Process Model:** Incremental Lifecycle Model  

---

## 1. Aim
To formulate a comprehensive, one-page Software Development Life Cycle (SDLC) engineering plan for an online grocery ordering platform with delivery time slots and intelligent out-of-stock product substitution, establishing milestones, deliverables, and role assignments across small, usable increments.

## 2. SDLC Incremental Delivery Schedule

```
+-------------------------------------------------------------------------------------------------+
|                                 FRESHCART 28-DAY SDLC SCHEDULE                                  |
+-------------------------------------------------------------------------------------------------+
|  Increment 1 (Days 1–7): Foundation & Catalog Browsing                                          |
|  - Scope: Product database schema, catalog browsing, shopping basket, responsive web UI.       |
|  - Key Deliverable: Deployable web catalog with local SQLite persistence.                       |
+-------------------------------------------------------------------------------------------------+
|  Increment 2 (Days 8–14): Prototype Module — Substitution Logic                                 |
|  - Scope: Out-of-stock detection, category-based candidate ranking, price tolerance cap (20%),  |
|           allergen safety filter, customer Accept/Reject decisioning.                           |
|  - Key Deliverable: Fully tested `substitution.py` module with 85%+ PyTest coverage.            |
+-------------------------------------------------------------------------------------------------+
|  Increment 3 (Days 15–21): Slot Booking & Order Fulfillment Workflow                            |
|  - Scope: Delivery slot capacity enforcement (10 orders/slot), order confirmation, customer      |
|           dietary profile tracking, checkout integration.                                       |
|  - Key Deliverable: Complete end-to-end checkout flow tested with Selenium automation.           |
+-------------------------------------------------------------------------------------------------+
|  Increment 4 (Days 22–28): Quality Assurance, DevOps & Health Monitoring                         |
|  - Scope: Docker packaging, Jenkins CI/CD pipeline, SonarQube static analysis, `/health` probe. |
|  - Key Deliverable: Hardened production container image (`freshcart:v1.0.0`) and audit reports. |
+-------------------------------------------------------------------------------------------------+
```

## 3. Team Role Assignments

| Engineering Role | Assigned Student / Persona | Core Responsibilities |
| :--- | :--- | :--- |
| **Project Lead & Architect** | Likhith Gowda M S | Overall system architecture, SQLite data modeling, and process coordination. |
| **Backend & Algorithm Engineer** | Likhith Gowda M S | Implementation of `suggest_substitution` ranking logic, price caps, and allergen filters. |
| **Frontend & UI Developer** | Student Peer 1 | Responsive Bootstrap 5 interface, cart badges, and substitution comparison cards. |
| **QA & Test Automation Engineer**| Student Peer 2 | PyTest test suite, Selenium end-to-end browser scripts, and defect tracking. |
| **DevOps & Quality Engineer** | Student Peer 3 | Dockerfile optimization, Jenkinsfile CI pipeline, and SonarQube quality gates. |

## 4. Conclusion
The Incremental SDLC plan establishes a clear 28-day delivery roadmap. By isolating the **Substitution Logic Prototype** into Increment 2, critical food safety rules and pricing thresholds are rigorously verified before integrating customer slot booking and production container deployment.
