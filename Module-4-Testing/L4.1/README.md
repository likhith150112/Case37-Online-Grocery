# Lab Experiment L4.1 — Exploratory Testing Session Notes

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Method:** Session-Based Test Management (SBTM) | **Duration:** 20 Minutes  

---

## 1. Test Charter
- **Charter:** *Explore out-of-stock cart handling, substitution candidate presentation, and delivery slot capacity limits to discover usability friction, edge-case crashes, and visual inconsistencies.*
- **Tester:** Likhith Gowda M S  
- **Environment:** Google Chrome 131, Windows 11, Local Flask Backend on Port 5000  
- **Session Duration:** 20 Minutes (10:00 AM – 10:20 AM IST)  

---

## 2. Session Execution & Exploration Log

| Time Mark | Action & Test Path Explored | Expected System Reaction | Actual Observed Behavior | Defect / Note |
| :---: | :--- | :--- | :--- | :---: |
| **00:00 - 04:00** | Launched homepage; searched for `"milk"` and `"butter"`. Added in-stock item (MIL-001). | Item added with green toast; cart badge updates from 0 to 1. | As expected. Quick response, clear visual badge. | **PASS** |
| **04:00 - 08:00** | Added out-of-stock item `MIL-002` (Amul Taaza Milk). Navigated to `/cart`. | Cart displays out-of-stock warning banner pointing to substitution review. | Warning banner displayed clearly with amber alert. | **PASS** |
| **08:00 - 12:00** | Navigated to `/substitutions`. Inspected side-by-side comparison of `MIL-002` vs `MIL-001`. | Replacement shows price delta (-₹10.00), tag matches, and Accept/Reject buttons. | Found minor visual bug: on very narrow mobile screens ($320\text{px}$), the comparison arrow overlapped button text. | **BUG-01 (Minor UI)** |
| **12:00 - 16:00** | Clicked "Accept Substitute". Checked cart state. | Cart replaces `MIL-002` with `MIL-001`. Total recalculated. | As expected. Substitution note tracked in session. | **PASS** |
| **16:00 - 20:00** | Attempted to select the full `Evening Slot (05:00 PM – 07:00 PM)` during checkout. | Radio button disabled; prevents booking. | Radio button disabled with red `[FULL]` badge. Cannot proceed until valid morning/night slot selected. | **PASS** |

---

## 3. Discovered Defects and Improvements

1. **Defect BUG-01 (Minor UI Wrapping):** On mobile viewports $< 360\text{px}$, the arrow icon between original and substitute items had insufficient margin. **Remediation:** Added `d-md-none` responsive spacing classes in `substitutions.html`.
2. **Improvement IMP-01 (Usability):** Added a link directly from product detail page to show alternatives when a product is out of stock, eliminating the need to add to cart first.

---

## 4. Conclusion
The 20-minute exploratory testing session verified the stability of the shopping cart and substitution workflow. Critical business constraints (blocking full delivery slots and swapping out-of-stock items) behaved robustly under human interaction.
