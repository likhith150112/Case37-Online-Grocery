# Part 2: Theory Answers — Module 5: AI-Powered Quality Assurance and Ethical Development

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Quality Assurance, Reliability & Ethics | **Standards:** ISO/IEC 25010, SonarQube  

---

### T5.1: Software Quality Attributes (ISO/IEC 25010) and Quantitative Reliability Metrics

The **ISO/IEC 25010 Product Quality Model** categorizes software quality into eight foundational characteristics:

```
+-----------------------------------------------------------------------------------+
|                        ISO/IEC 25010 Quality Model                                |
+-----------------------------------------------------------------------------------+
| 1. Functional Suitability : Accurate substitution ranking, slot booking.          |
| 2. Performance Efficiency : Sub-50ms ranking latency, fast DB queries.           |
| 3. Compatibility          : Cross-browser responsive UI (Bootstrap 5).            |
| 4. Usability              : Clear out-of-stock banners, Accept/Reject options.    |
| 5. Reliability            : 98% success rate, ACID transactions, healthchecks.    |
| 6. Security               : Input validation, dynamic secret keys, zero PII.      |
| 7. Maintainability        : Modular dataclasses, clean PEP 8, 85% test coverage.  |
| 8. Portability            : Containerized execution on Docker across platforms.   |
+-----------------------------------------------------------------------------------+
```

#### Core Mathematical Quality Metrics in FreshCart:

1. **Defect Density ($D$):**
   $$D = \frac{\text{Total Confirmed Defects}}{\text{Size of Software in Thousand Lines of Code (KLOC)}}$$
   - For FreshCart codebase ($\approx 0.58\text{ KLOC}$ of core logic) with 2 defects detected and fixed during development:
     $$D = \frac{2}{0.58} \approx \mathbf{3.45\text{ defects/KLOC}}$$
2. **Failure Rate ($F$):**
   $$F = \frac{\text{Failed Runs}}{\text{Total Test Executions}} \times 100\%$$
   - In 50 consecutive automated end-to-end runs (Experiment L5.1), 1 failure occurred due to temporary SQLite busy lock:
     $$F = \frac{1}{50} \times 100\% = \mathbf{2.0\%} \implies \text{Observed Reliability} = \mathbf{98.0\%}$$

---

### T5.2: Static Code Analysis, SonarQube Architecture, and Quality Gates

Static code analysis analyzes source code without executing it, checking syntax, data flows, and dependencies against rulesets.

#### 1. The Three Finding Categories in SonarQube:
- **Bugs:** Coding mistakes that will lead to runtime crashes or incorrect outputs (e.g. `isinstance` omission or off-by-one errors).
- **Vulnerabilities / Security Hotspots:** Flaws that expose the application to compromise (e.g. hardcoded secrets or unescaped user inputs).
- **Code Smells:** Maintainability issues that do not break functionality but make the code convoluted and difficult to modify (e.g., duplicate code strings, excessive cognitive complexity).

#### 2. FreshCart SonarQube Quality Gate Criteria:
- **Coverage:** $\ge 80.0\%$ on new code (FreshCart achieved $85\%$).
- **Bugs:** $0$ Blocker or Critical bugs.
- **Vulnerabilities:** $0$ Security vulnerabilities.
- **Security Hotspots:** $100\%$ reviewed and cleared.
- **Duplicated Lines:** $< 3.0\%$ duplication across all files.

---

### T5.3: AI Code Review vs. Human Peer Review

| Review Dimension | AI Code Review (ChatGPT / Copilot / GitHub PR Bot) | Human Peer Review (Senior Engineer) |
| :--- | :--- | :--- |
| **Speed & Throughput** | Instantaneous (< 10 seconds for 500 lines). | Hours to days depending on reviewer workload. |
| **Syntactic Pattern Matching** | Exceptional at spotting missing docstrings, PEP 8 formatting, and common regex anti-patterns. | Moderate; humans get fatigued reviewing repetitive syntax. |
| **Business Logic & Context** | **Poor / Blind:** Does not know store delivery truck capacities or regional food safety laws. | **Superior:** Understands commercial context, business objectives, and customer impact. |
| **Systemic Architecture** | Evaluates isolated functions; misses system-wide lock contention or distributed race conditions. | Evaluates how the function affects overall system health and database performance. |

#### Synergetic Review Policy:
FreshCart enforces a **two-tier review policy**: First, automated tools and AI review code for syntax, coverage, and style. Second, a human engineer conducts a mandatory peer review to verify business rules, security, and ethics.

---

### T5.4: Software Reliability Engineering, MTBF/MTTR, and Availability

#### 1. Core Reliability Formulas:
- **Mean Time Between Failures (MTBF):** The average operational uptime between consecutive system crashes:
  $$\text{MTBF} = \frac{\text{Total Operational Uptime}}{\text{Number of Failures}}$$
- **Mean Time to Repair (MTTR):** The average time required to diagnose, patch, and restore the service:
  $$\text{MTTR} = \frac{\text{Total Downtime}}{\text{Number of Failures}}$$
- **System Availability ($A$):**
  $$A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%$$

#### Application in FreshCart:
If the online grocery backend runs continuously for 30 days ($720\text{ hours}$) and experiences two brief service restarts lasting 15 minutes each ($0.5\text{ hours}$ total downtime):
$$\text{MTBF} = \frac{719.5}{2} = 359.75\text{ hours}, \quad \text{MTTR} = \frac{0.5}{2} = 0.25\text{ hours} \ (15\text{ mins})$$
$$A = \frac{359.75}{359.75 + 0.25} = \frac{359.75}{360.00} = \mathbf{99.93\% \ (Three Nines)}$$

---

### T5.5: Ethical AI Engineering: Demographic Fairness, Transparency, and Algorithmic Bias

#### 1. Algorithmic Discrimination in Retail:
AI recommendation and pricing algorithms frequently encode societal biases:
- **Price Discrimination:** Models might quote higher prices to users in specific postal codes or using specific devices (e.g. higher prices for iOS users). In basic food retail, this constitutes unethical price gouging.
- **Demographic Bias:** Algorithms trained on past purchase volumes might prioritize luxury items over basic staples for certain customer names or demographic groups.

#### 2. FreshCart Ethical Engineering Safeguards:
1. **Feature Blinding:** Sensitive customer attributes (name, gender, demographic labels) are strictly excluded from the substitution ranking algorithm. The function `suggest_substitution` accepts only item category, price, in-stock status, and explicit dietary flags.
2. **Fairness Testing (Experiment L5.5):** Synthetic user profiles varying only in name (*Aarav* vs *Ananya* vs *Zaid*) or gender are passed through the substitution engine. The system guarantees $100\%$ identical candidate rankings and prices across all demographic profiles.
3. **Transparent Price Deltas:** Any price variation between the original and substitute product is explicitly displayed with green/red badges before payment confirmation.
