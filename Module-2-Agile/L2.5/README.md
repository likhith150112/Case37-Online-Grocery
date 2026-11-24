# Lab Experiment L2.5 — Support Ticket Processing: AI Summarization, Duplicate Detection and Accuracy Calculation

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Tool:** ChatGPT  

---

## 1. Aim
To simulate a real-world store support backlog of 10 customer and picker tickets, utilize ChatGPT to automatically summarize issues and detect duplicate bug reports, and calculate the quantitative accuracy of the AI triage process.

---

## 2. Dataset of Ten Support and Bug Tickets

| Ticket ID | Raw Stakeholder Ticket Description | Category | Priority |
| :---: | :--- | :---: | :---: |
| **TCK-01** | *"Customer in Indiranagar says they ordered Amul Taaza 1L but got Nandini Milk without any SMS warning."* | Substitution | High |
| **TCK-02** | *"When I try to pick order FC-1049, the item Amul Milk is showing replaced with Nandini Milk. Did customer approve this?"* | Substitution | High |
| **TCK-03** | *"Delivery slot for 5 PM to 7 PM is locked and showing red [FULL] badge even though I want to order."* | Slot Booking | Medium |
| **TCK-04** | *"Cannot select evening delivery time (5 PM - 7 PM). Radio button is greyed out."* | Slot Booking | Medium |
| **TCK-05** | *"Customer with severe peanut allergy asked if our oat cookies have nuts. Need allergen flag."* | Food Safety | High |
| **TCK-06** | *"I tried to buy Basmati rice, it suggested Daawat rice which costs ₹5 more. App didn't show the difference clearly."* | Pricing / UI | Medium |
| **TCK-07** | *"App charged ₹30 delivery fee even though my cart total was ₹520."* | Billing Bug | High |
| **TCK-08** | *"Checkout failed with 500 error when database was busy during peak picking hours."* | Infrastructure | Blocker |
| **TCK-09** | *"Evening slot 17:00 to 19:00 cannot be selected on mobile screen."* | Slot Booking | Medium |
| **TCK-10** | *"Substitute item suggestion showed Almond Milk for a dairy milk customer who checked avoid nuts."* | Food Safety | Blocker |

---

## 3. AI Summarization and Duplicate Detection Analysis

### Prompt Given to ChatGPT:
```
Analyze the 10 grocery support tickets above.
1. Provide a one-sentence summary for each ticket.
2. Group and identify all DUPLICATE or overlapping bug reports.
3. Suggest the root cause for each duplicate cluster.
```

### AI Analysis Results:

#### Identified Duplicate Clusters:
1. **Cluster A (Evening Slot Capacity Lock):**
   - *Tickets:* `TCK-03`, `TCK-04`, `TCK-09`.
   - *AI Finding:* Identified as exact duplicates describing intended behavior: Evening slot reaches 10-order capacity limit and disables itself. Not a software defect, but requires UI tooltip explaining capacity limit.
   - *Human Verification:* **TRUE POSITIVE (Accurate grouping).**
2. **Cluster B (Unconfirmed Substitution Inquiries):**
   - *Tickets:* `TCK-01`, `TCK-02`.
   - *AI Finding:* Duplicates concerning customer notification of accepted substitutions.
   - *Human Verification:* **TRUE POSITIVE (Accurate grouping).**
3. **Cluster C (Allergen Safety Incident):**
   - *Tickets:* `TCK-05`, `TCK-10`.
   - *AI Finding:* Grouped as duplicates.
   - *Human Verification:* **FALSE POSITIVE.** `TCK-05` is a general feature request for cookies; `TCK-10` is a critical active software bug where an almond product was suggested to a nut-allergic customer. They must be handled as separate tickets with different severities.

---

## 4. Quantitative Accuracy Calculation

$$\text{Duplicate Detection Accuracy} = \frac{\text{Correctly Classified Pairs / Clusters}}{\text{Total Evaluated Clusters}} \times 100\%$$

- Total Clusters Identified by AI: **3**
- Correctly Grouped Clusters (True Positives): **2** (Cluster A and Cluster B)
- Incorrectly Grouped Clusters (False Positives): **1** (Cluster C)
- **AI Duplicate Detection Accuracy:**
  $$\text{Accuracy} = \frac{2}{3} \times 100\% = \mathbf{66.7\%}$$

- **Summary Accuracy:** 10 / 10 one-sentence summaries were accurate $\implies \mathbf{100\%}$ summarization accuracy.

---

## 5. Conclusion
ChatGPT achieved **100% accuracy** in syntactic summarization and **66.7% accuracy** in duplicate triage. The exercise demonstrates that while AI rapidly groups tickets with similar keywords ("allergy", "slot"), a human QA triage engineer is vital to distinguish between a general user inquiry and a blocker safety defect.
