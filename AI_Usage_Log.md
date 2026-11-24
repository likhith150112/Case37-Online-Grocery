# Appendix A — Master AI Usage Log

**Student Name:** Likhith Gowda M S  
**Roll Number:** 37  
**USN:** ENG24CS0105  
**Section:** 5B  
**Institution:** Dayananda Sagar University, Bengaluru  
**Subject:** AI in Software Engineering  
**Case Number:** 37 — Online Grocery Ordering and Slot-Based Delivery  
**Primary AI Tool Specified:** ChatGPT (OpenAI GPT-4o)  

---

## 1. Overview and Engineering Protocol
This document records all instances where Generative AI was used to assist during the software engineering lifecycle of Case 37. In accordance with university academic standards:
1. **No Real PII or Credentials:** No real customer identities, payment data, or private tokens were submitted to AI tools.
2. **Mandatory Human Verification:** Every AI-generated requirement, estimation, code snippet, and test case was subjected to line-by-line review, compilation, execution, and debugging by the student engineer.
3. **Traceability:** Prompts, modifications, and acceptance/rejection decisions are fully documented below.

---

## 2. Chronological AI Interaction Log

| Log ID | SDLC Phase & Date | AI Tool Used | Prompt Provided to AI Tool | Summary of AI Output | Human Engineering Evaluation & Corrections | Final Decision |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| **LOG-01** | Requirements Elicitation<br>*(10-Nov-2026)* | ChatGPT | *"Extract formal functional and non-functional requirements from the following raw store-staff WhatsApp messages: [staff messages on slot overload, milk stockouts, customer approval]."* | Drafted 5 functional requirements and 2 NFRs. Identified need for slot limits and customer approval. | AI omitted quantitative slot capacity numbers and left response time subjective. Refined criteria into testable metrics (10 orders/slot, $< 200\text{ ms}$). | **Accepted with Modifications** |
| **LOG-02** | Process Model Selection<br>*(11-Nov-2026)* | ChatGPT | *"Compare Waterfall, V-Model, Spiral, Agile, and Incremental for a grocery system with an intelligent substitution prototype module. Score each out of 10."* | Ranked Incremental and Agile top. Provided preliminary scoring criteria. | Adjusted weights to prioritize early working software and prototype safety isolation. Derived weighted decision matrix (9.25/10 for Incremental). | **Accepted with Modifications** |
| **LOG-03** | Agile Planning<br>*(12-Nov-2026)* | ChatGPT | *"Decompose Epic 'Order Fulfillment & Substitution' into 5 INVEST user stories with story point estimates (Fibonacci) and Kanban WIP limits."* | Proposed US-01 to US-05 with estimates (3, 3, 5, 2, 2). Suggested WIP limits: In Progress=3, Review=2. | Team Planning Poker increased US-02 (Stock Check) from 3 to 5 points due to SQLite ACID concurrency race conditions. Accepted WIP limits. | **Accepted with Modifications** |
| **LOG-04** | Core Coding (Prototype)<br>*(13-Nov-2026)* | ChatGPT | *"Act as a Senior Python Architect. Use dataclasses to write `suggest_substitution(requested, catalog, ...)` enforcing category match, 20% price cap, and allergen avoidance."* | Generated dataclass structures and sorting function using price deltas. | **Identified Flaw:** Code accepted negative prices ($-₹50 \le \text{limit}$). Fixed by adding `if candidate.price <= 0: continue` and `.casefold()` on allergens. | **Accepted with Fixes** |
| **LOG-05** | Test Generation<br>*(14-Nov-2026)* | ChatGPT | *"Generate 10 unit test cases for the grocery substitution module covering nominal, boundary, and negative scenarios."* | Suggested 10 test cases including in-stock return, price limits, allergen filtering, and empty catalogs. | Discovered AI missed negative threshold argument tests (`max_price_increase < 0`) and non-Product type errors. Implemented missing cases in PyTest. | **Accepted (80% Accuracy)** |
| **LOG-06** | CI/CD Pipeline<br>*(15-Nov-2026)* | ChatGPT | *"Draft a declarative Jenkinsfile for a Python Flask application that runs pytest with coverage >= 80%, SonarQube, and builds a Docker image."* | Created 6-stage pipeline script with environment variables and post actions. | Verified stage syntax; adjusted Docker tag naming convention and local artifact archiving paths. | **Accepted** |
| **LOG-07** | Docker Packaging<br>*(16-Nov-2026)* | ChatGPT | *"Write an optimized Dockerfile for Python 3.14 Flask application with curl healthchecks and non-root execution."* | Provided multi-directive Dockerfile based on `python:3.14-slim`. | Verified line-by-line; added metadata labels for Case 37, USN, and student name; confirmed healthcheck probe works with `/health`. | **Accepted** |
| **LOG-08** | Usability & Ethics<br>*(17-Nov-2026)* | ChatGPT | *"Evaluate ethical risks of AI dynamic price personalization in grocery e-commerce and suggest mitigation rules."* | Outlined price discrimination risks on essential foods and suggested algorithmic feature blinding. | Formalized 4-point Ethical AI Charter: uniform base pricing, transparent price deltas, demographic blinding, and human governance. | **Accepted** |

---

## 3. Summary of AI Value and Limitations
- **Primary Value Delivered by ChatGPT:** Rapid structuring of informal requirements, boilerplate elimination in dataclass definitions, and brainstorming boundary test permutations.
- **Critical Limitations Observed:** Tendency to overlook concurrency hazards in multi-user databases, subtle boundary flaws (negative prices), and initial case-sensitivity blind spots in string set intersections.
- **Conclusion:** ChatGPT served as an effective cognitive accelerator, but rigorous software engineering discipline, static analysis, and local testing were indispensable to produce reliable, safe software.

