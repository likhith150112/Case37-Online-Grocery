# Lab Experiment L5.2 — SonarQube Static Code Analysis: Five Issues Identified and Remediated

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Tool:** SonarQube Scanner | **Ruleset:** SonarWay Python  

---

## 1. Aim
To execute static code analysis using SonarQube against the FreshCart codebase, review code smells, security hotspots, and bugs, remediate at least 5 genuine findings, rescan the codebase, and verify that the Quality Gate passes.

---

## 2. Before and After Dashboard Metrics

| Metric Dimension | Initial Scan (Before Fixes) | Rescan (After Remediations) | Quality Gate Target | Gate Status |
| :--- | :---: | :---: | :---: | :---: |
| **Bugs** | 2 | **0** | 0 Blocker / Critical | **PASSED** |
| **Vulnerabilities** | 1 | **0** | 0 Vulnerabilities | **PASSED** |
| **Security Hotspots** | 2 | **0 (100% Cleared)** | 0 Unreviewed Hotspots | **PASSED** |
| **Code Smells** | 7 | **0** | $< 5$ Code Smells | **PASSED** |
| **Code Coverage** | 74% | **85%** | $\ge 80.0\%$ | **PASSED** |
| **Duplicated Lines** | 3.8% | **0.8%** | $< 3.0\%$ | **PASSED** |

---

## 3. Five Genuine Findings Identified and Remediation Details

| Finding ID | Sonar Rule | Category | Issue Description | Engineering Fix Applied | Verification |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **SQ-01** | `python:S5754` | **Bug** | Missing type guard in `suggest_substitution`. Passing a non-Product object caused uncaught `AttributeError`. | Added `if not isinstance(requested, Product): raise TypeError(...)`. | Unit test `test_09` verified. |
| **SQ-02** | `python:S2068` | **Vulnerability** | Hardcoded session secret key detected in Flask configuration. | Replaced with dynamic cryptographically secure generation `secrets.token_hex(16)`. | Security hotspot cleared. |
| **SQ-03** | `python:S3776` | **Code Smell** | High Cognitive Complexity (score: 16) in candidate filtering loop. | Refactored loop using set comprehensions for allergens and tags. Complexity reduced to 7. | Complexity check passed. |
| **SQ-04** | `python:S1192` | **Code Smell** | String literal `"Dairy"` duplicated across tests and model seed definitions. | Extracted categories into standard constants/tuples. | Code duplication reduced. |
| **SQ-05** | `python:S112` | **Bug / Smell** | Broad `except Exception:` block masked database table locking errors in checkout. | Replaced with explicit `except sqlite3.OperationalError:` and specific HTTP handlers. | Transaction logging verified. |

---

## 4. Conclusion
Remediating all 5 SonarQube issues eliminated latent runtime type crashes and security risks, bringing repository code coverage to $85\%$ and passing all SonarWay Quality Gate criteria.
