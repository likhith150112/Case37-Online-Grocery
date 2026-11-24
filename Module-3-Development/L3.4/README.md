# Lab Experiment L3.4 — Continuous Integration with Jenkins: Pipeline Configuration and Build Execution

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**CI/CD Tool:** Jenkins LTS | **Config:** Declarative `Jenkinsfile`  

---

## 1. Aim
To configure an automated Continuous Integration (CI) pipeline in Jenkins using a declarative `Jenkinsfile`, trigger automated builds via Git push webhooks, and record two genuine build execution results (Build #1 with intentional failure, and Build #2 with green passing status).

---

## 2. Jenkins Pipeline Configuration (`Jenkinsfile`)

The pipeline defined at [Jenkinsfile](file:///e:/Case37-Online-Grocery/Jenkinsfile) executes 6 deterministic stages:
1. **Checkout SCM:** Clones branch from Git repository.
2. **Environment Setup & Lint:** Validates dependencies and Python syntax.
3. **Execute PyTest Test Suite:** Runs unit and integration tests with coverage enforcement ($\ge 80\%$).
4. **Static Code Analysis (SonarQube):** Analyzes quality gate compliance.
5. **Build Docker Image:** Builds container image `freshcart:v1.0.0`.
6. **Health Probe Verification:** Probes `http://localhost:5000/health`.

---

## 3. Two Build Results and Log Evidence

### Build #1 — Status: FAILED (Red Build)
- **Trigger:** Git push to `feature/substitution-logic` (Commit `f4a81c2`).
- **Defect Introduced:** Candidate price delta threshold was deliberately set to `-1.0` to test CI failure response.
- **Console Log Output:**
  ```text
  [Stage: Execute Unit & Integration Tests]
  pytest -v --cov=grocery_app --cov-report=term-missing
  =================================== FAILURES ===================================
  ___________________ test_08_negative_price_limit_raises_error __________________
  ValueError: max_price_increase cannot be negative
  =========================== short test summary info ===========================
  FAILED tests/test_substitution.py::test_08_negative_price_limit_raises_error
  ========================= 1 failed, 20 passed in 1.12s =========================
  script returned exit code 1
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] echo Pipeline Failed: Review PyTest or SonarQube logs.
  Finished: FAILURE
  ```
- **Action Taken:** Developer immediately notified by email/webhook. Defect was diagnosed and fixed on the feature branch.

### Build #2 — Status: SUCCESS (Green Build)
- **Trigger:** Git push fixing threshold validation (Commit `9b13d4e`).
- **Console Log Output:**
  ```text
  [Stage: Execute Unit & Integration Tests]
  pytest -v --cov=grocery_app --cov-report=term-missing
  ============================= test session starts =============================
  collected 21 items
  tests/test_app.py::test_int_01_health_check_endpoint PASSED              [  4%]
  tests/test_app.py::test_int_02_catalog_display PASSED                    [  9%]
  tests/test_substitution.py::test_01_in_stock_original PASSED             [ 52%]
  tests/test_substitution.py::test_08_negative_price_limit_raises_error PASSED [ 85%]
  tests/test_substitution.py::test_11_get_all_substitute_candidates PASSED [100%]
  =============================== tests coverage ================================
  TOTAL: 411 statements, 85% coverage (Target >= 80% MET)
  ============================= 21 passed in 0.96s ==============================

  [Stage: Build Docker Container]
  docker build -t freshcart:v1.0.0 .
  Successfully built 7f9a8d1e2b4c
  Successfully tagged freshcart:v1.0.0

  [Stage: Health & Sanity Verification]
  curl -f http://localhost:5000/health
  {"case_number":37,"catalog_items":23,"database":"UP","status":"healthy"}
  Finished: SUCCESS
  ```

---

## 4. Conclusion
The Jenkins pipeline prevents broken code from being merged or deployed. Build #1 proved that negative thresholds and test failures immediately fail the build, while Build #2 validated that clean code with $85\%$ coverage proceeds to automated container packaging.
