# Lab Experiment L5.1 — Defect Density and Quantitative Reliability Measurement over 50 Executions

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module Focus:** Quality Assurance & Reliability Engineering  

---

## 1. Aim
To execute 50 automated end-to-end e-commerce order cycles (health check, cart addition, out-of-stock detection, substitution recommendation, and slot booking) using `reliability_test.py`, record failure rates, compute Defect Density, and calculate system reliability.

---

## 2. Experimental Execution Evidence

Script: `Module-5-Quality-Assurance/L5.1/reliability_test.py`  
Output Log: `Module-5-Quality-Assurance/L5.1/reliability_50_runs.log`  

### Terminal Summary Output:
```text
=== Starting 50-Run Software Reliability & Defect Density Experiment ===
Target: FreshCart E-Commerce Order Flow | Total Runs: 50

Run 01: SUCCESS (HTTP 200, Sub=MIL-001, Latency=0.022s)
Run 02: SUCCESS (HTTP 200, Sub=MIL-001, Latency=0.014s)
...
Run 49: SUCCESS (HTTP 200, Sub=MIL-001, Latency=0.009s)
Run 50: SUCCESS (HTTP 200, Sub=MIL-001, Latency=0.009s)

=== 50-Run Reliability Results Summary ===
Total Runs Executed : 50
Successful Runs     : 50 (100.0%)
Failed Runs         : 0 (0.0%)
Observed Reliability: 100.0%
Total Execution Time: 0.43 seconds
Codebase Size       : 0.411 KLOC
Defect Density      : 2.43 defects/KLOC
```

---

## 3. Mathematical Metric Formulations & Calculations

### 1. Defect Density ($D$):
$$\text{Defect Density} = \frac{\text{Confirmed Defects Detected}}{\text{Size of Codebase in KLOC}}$$
- Confirmed defects identified during testing cycle = **1** (Negative price threshold edge case)
- Codebase size ($N_{LOC}$) = **411 lines of code** ($0.411\text{ KLOC}$)
$$D = \frac{1}{0.411} \approx \mathbf{2.43\text{ defects / KLOC}}$$
*(Industry benchmark for commercial web systems is $< 5.0\text{ defects/KLOC}$)*.

### 2. Failure Rate ($F$) & Reliability ($R$):
$$F = \frac{\text{Failed Runs}}{\text{Total Executions}} \times 100\% = \frac{0}{50} \times 100\% = \mathbf{0.0\%}$$

$$R = 100\% - F = \mathbf{100.0\% \text{ Observed Reliability}}$$

---

## 4. Conclusion
Across 50 rapid sequential executions, the FreshCart backend maintained $100\%$ availability with an average cycle latency of $\approx 9\text{ ms}$, validating that SQLite transactions and in-memory session operations perform reliably without connection leaks or deadlocks.
