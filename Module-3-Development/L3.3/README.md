# Lab Experiment L3.3 — GitHub Branch Protection Rules, Pull Request Lifecycle and Code Review Governance

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**VCS:** Git & GitHub  

---

## 1. Aim
To configure GitHub branch protection rules on the `master` / `main` branch, simulate a feature branch pull request (`feature/substitution-logic`), demonstrate that direct pushes and unreviewed PRs are strictly blocked, and guide the student through independent reviewer approval.

---

## 2. GitHub Branch Protection Configuration Guide

To protect production stability, the following rules are enforced on the remote GitHub repository:

```
Settings -> Branches -> Add branch protection rule:
- Branch name pattern: master (or main)
  [x] Require a pull request before merging
      [x] Require approvals: 1 (At least one peer reviewer must sign off)
      [x] Dismiss stale pull request approvals when new commits are pushed
      [x] Require review from Code Owners
  [x] Require status checks to pass before merging
      [x] Require branches to be up to date before merging
      Status checks:
      - continuous-integration/jenkins/pr-merge (PyTest pass >= 80% coverage)
      - sonarqube/quality-gate (Zero Blocker/Critical issues)
  [x] Do not allow bypassing the above settings (Enforce for administrators)
  [x] Restrict who can push to matching branches (Block direct git push)
```

---

## 3. Pull Request Lifecycle Walkthrough

```
Step 1: Developer creates feature branch
$ git checkout -b feature/substitution-logic

Step 2: Commit verified code
$ git add grocery_app/substitution.py tests/test_substitution.py
$ git commit -m "feat(substitution): implement rule-based item replacement with allergen safety"

Step 3: Push feature branch to remote GitHub
$ git push origin feature/substitution-logic

Step 4: Open Pull Request on GitHub UI (PR #1)
Target: master  <-- Source: feature/substitution-logic
Status: "Merging is BLOCKED - 1 review required, CI checks pending"

Step 5: Independent Peer Reviewer Action
Peer reviewer logs into GitHub, reviews the code diff, verifies PyTest execution, and clicks:
"Review changes" -> "Approve"

Step 6: CI Status Checks Pass
Jenkins reports: "continuous-integration/jenkins/pr-merge - SUCCESS"

Step 7: Merge Button Enabled
Branch can now be cleanly merged into master using Squash and Merge or Rebase.
```

---

## 4. Student Guide for Independent Peer Review
When submitting this assignment:
1. Create a public or private GitHub repository named `Case37-Online-Grocery`.
2. Push your `master` branch and `feature/substitution-logic` branch.
3. Invite a classmate (e.g. your lab partner or section peer) as a Collaborator with Read/Write access.
4. Have your collaborator review PR #1 and click **Approve Changes** with a comment: *"Reviewed substitution algorithm, allergen filters verified, PyTest tests pass."*
5. Capture a screenshot of the approved PR showing the green checkmark for submission evidence.

---

## 5. Conclusion
Branch protection rules ensure that no untested or unreviewed code enters production, creating an auditable commit history and guaranteeing that all Definition of Done criteria are satisfied before release.
