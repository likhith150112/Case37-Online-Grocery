# Part 2: Theory Answers — Module 1: Software Engineering, SDLC and Process Models

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Process Model:** Incremental | **AI Tool:** ChatGPT | **Prototype:** Substitution Logic  

---

### T1.1: Software Engineering and the Software Development Life Cycle (SDLC)

#### Definition and Core Purpose
Software engineering is defined by IEEE as *"the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software."*

In the context of the **Online Grocery Application (Case 37)**, software engineering transforms ad-hoc coding into an architected, verifiable system. Grocery platforms deal with perishable inventory, real-time delivery slot contention, food allergy liabilities, and financial payment handling. Without disciplined engineering, problems such as overbooked delivery slots, incorrect billing of substitute items, and inventory race conditions would cripple store operations.

#### SDLC Phases and Key Engineering Artifacts in Online Grocery:

```
+---------------+     +---------------+     +---------------+     +---------------+
| 1. Planning   | --> | 2. Req. Eng.  | --> | 3. System Des.| --> | 4. Development|
| Feasibility   |     | SRS (FRs/NFRs)|     | ER / Schemas  |     | Python/Flask  |
+---------------+     +---------------+     +---------------+     +---------------+
                                                                          |
+---------------+     +---------------+     +---------------+             |
| 7. Maintenance| <-- | 6. Deployment | <-- | 5. Verification|<------------+
| Monitoring    |     | Docker/CI-CD  |     | PyTest/Selenium|
+---------------+     +---------------+     +---------------+
```

1. **Planning & Feasibility:** Defines the economic, technical, and legal viability. For Case 37, this established that a slot-based local delivery model with an intelligent substitution engine was technically viable using Python, SQLite, and Flask.
2. **Requirements Engineering:** Elicits and documents functional requirements (FR-01 to FR-05) and non-functional requirements (NFR-01 to NFR-02) into an approved Software Requirements Specification (SRS).
3. **System Design:** Architects database schemas (`products`, `delivery_slots`, `orders`), component diagrams, and the substitution ranking pipeline.
4. **Implementation (Coding):** Translates architectural designs into clean, modular code (`grocery_app/substitution.py`, `app.py`).
5. **Testing & Verification:** Executes unit tests (PyTest), end-to-end browser journeys (Selenium), and static analysis (SonarQube) to guarantee $\ge 80\%$ test coverage.
6. **Deployment:** Packages the application into a Docker container and triggers CI/CD automation through Jenkins.
7. **Maintenance & Monitoring:** Operates continuous health probes (`/health`), logs latency metrics, and patches inventory anomalies.

---

### T1.2: Evaluation and Ranking of Five Process Models for Online Grocery

Five classic process models were evaluated for Case 37 based on five engineering criteria: Requirements Flexibility, Delivery Speed, Risk Management, Architectural Discipline, and Customer Collaboration.

#### Process Model Ranking Table:

| Rank | Process Model | Fit Score (1–10) | Strengths in Online Grocery | Weaknesses in Online Grocery |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Incremental Model** | **9.6** | Delivers working software in small, usable increments. Core catalog and slot reservation can go live in Increment 1, while advanced AI substitution logic is refined in Increment 2. | Requires careful initial system architecture to ensure subsequent increments integrate smoothly. |
| **2** | **Agile (Kanban)** | **9.2** | Excellent for managing the continuous flow of orders and rapid changes in stock availability; enforces WIP limits. | Can suffer from scope creep if release milestones are not tracked with clear Definition of Done. |
| **3** | **Spiral Model** | **7.8** | Risk-driven approach that is ideal if the prototype involves high-cost third-party hardware or unknown machine learning APIs. | Excessive management overhead, prototyping phases, and cost for a student or small store grocery application. |
| **4** | **V-Model** | **6.5** | Rigorous verification and validation mapping at every stage (Unit testing directly mirrors low-level design). | Highly inflexible; difficult to adjust substitution rules or slot times once requirements are locked. |
| **5** | **Waterfall Model** | **4.2** | Highly structured and documented stage-gate process. | Completely unsuitable; assumes all grocery requirements are frozen upfront. Feedback is received too late. |

**Justification for Incremental Model as #1:**
The Incremental Model enables the grocery chain to deliver a functional minimum viable product (catalog browsing and slot checkout) to actual customers in weeks, generating early revenue. The complex, safety-critical **Substitution Logic module** is developed and verified in the second increment, allowing focused PyTest test-driven development, allergen isolation, and customer feedback without risking core ordering functions.

---

### T1.3: AI-Driven Software Lifecycle vs. Traditional SDLC

The integration of Generative AI tools (such as ChatGPT and GitHub Copilot) creates an **AI-Augmented SDLC**, but it does not replace human engineering responsibility.

```
Traditional SDLC vs AI-Augmented SDLC:
Traditional: [Human Elicitation] ---> [Human Drafting] --------> [Human Coding] --------> [Human Testing]
AI-Driven:   [Staff Chat Notes]  ---> [ChatGPT Drafts SRS]  ---> [Copilot Drafts Code] -> [AI Test Suggestions]
                     │                       │                         │                         │
                     ▼                       ▼                         ▼                         ▼
             [Human Interview]       [Human Ambiguity Filter]  [Code Review & Unit Test] [Risk Matrix Validation]
```

#### Phase-by-Phase Comparison Table:

| SDLC Phase | Traditional SDLC Approach | AI-Augmented SDLC (Case 37) | Mandatory Human Checkpoint |
| :--- | :--- | :--- | :--- |
| **Requirements** | Business analysts conduct lengthy manual stakeholder interviews. | ChatGPT parses raw store-staff chat logs into structured draft user stories. | **Engineer validates** domain constraints (e.g. 20% price cap, delivery slot limits). |
| **Architecture** | Architect draws UML and ER models from scratch. | AI suggests entity schemas and dataclass structures. | **Engineer enforces** database normalization, primary keys, and ACID transactions. |
| **Coding** | Developers write all boilerplate, route handlers, and algorithms by hand. | Developer uses prompts to draft functions (`suggest_substitution`) and helpers. | **Line-by-line review** to eliminate hallucinations, negative price bugs, and security risks. |
| **Testing** | QA engineers write test scripts manually from specifications. | AI suggests boundary conditions, edge cases, and synthetic customer personas. | **QA executes** tests against live code; verifies passing assertions and code coverage $\ge 80\%$. |
| **Deployment** | DevOps engineers manually write Dockerfiles and CI scripts. | AI drafts `Jenkinsfile` and `Dockerfile` templates. | **DevOps validates** container base images, port exposures, and healthcheck probes. |

---

### T1.4: AI-Enabled Tools: GitHub Copilot, Tabnine, and ChatGPT

| Evaluation Parameter | GitHub Copilot | Tabnine | ChatGPT (OpenAI) |
| :--- | :--- | :--- | :--- |
| **Primary Paradigm** | Context-aware inline code autocompletion inside IDE (VS Code). | Privacy-focused inline code completion running locally or in private cloud. | Conversational reasoning, architectural explanation, requirements drafting, and code synthesis. |
| **Context Scope** | Active workspace files, open tabs, and function docstrings. | Local file context and trained language patterns. | Prompt window context (instructions, personas, few-shot examples). |
| **Best Used For** | Fast implementation of boilerplate, dataclasses, and PyTest assertions. | Enterprise environments with strict intellectual property isolation. | Drafting user stories from messy notes, debugging complex logic, explaining algorithms. |
| **Security & Privacy** | Code telemetry may be shared unless enterprise privacy controls are active. | High data privacy; models can run fully offline on-premise. | Public web sessions retain prompt data unless Zero Data Retention is active. |

#### Safe AI Usage Policy for Software Engineers:
1. **Never Expose Sensitive Data:** Never include production database passwords, personal customer identities (PII), API credentials, or proprietary pricing contracts in prompts.
2. **Verify Licensing & IP:** Review generated code snippets to ensure no GPL-contaminated or copyright-infringing code is introduced into commercial repositories.
3. **Human Accountability:** The human engineer signs off on all committed code. "The AI generated it" is never an acceptable explanation for a production defect.

---

### T1.5: Limits of AI-Assisted Requirements Engineering and Human Resolution

While Large Language Models excel at syntactic summarization, they exhibit critical failure modes in requirements engineering:
1. **Hallucination of Non-Existent Constraints:** AI may invent arbitrary delivery policies (e.g., claiming orders must be placed 48 hours in advance) that contradict actual store capabilities.
2. **Failure to Detect Stakeholder Contradictions:** If one picker states *"never replace items"* while a store manager states *"always substitute out-of-stock items to maximize sales"*, AI often merges both into contradictory requirements.
3. **Ambiguity and Un-testability:** AI frequently outputs subjective phrases such as *"the substitution engine must be fast, accurate, and user-friendly"* which cannot be objectively tested.

#### Systematic Human Engineering Resolution Framework:
- **Step 1: Disambiguation:** Convert vague statements into measurable criteria (e.g., *"fast"* becomes *"response time $< 50\text{ ms}$ for 5,000 SKUs"*).
- **Step 2: Conflict Resolution:** Interview primary stakeholders (Store Manager) to establish precedence: customer consent overrides automated item substitution.
- **Step 3: Testable Acceptance Criteria:** Frame requirements in Gherkin / Given-When-Then format (e.g., *Given an item is out of stock, When the customer reviews substitutions, Then only candidates within $\le 20\%$ price delta are presented*).
