# Case Task A — Incremental Lifecycle and AI-Assisted Requirements Engineering

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Process Model:** Incremental Model | **AI Assistance Tool:** ChatGPT  

---

## 1. Context and Problem Statement

Local supermarket chains face stiff competition from quick-commerce giants. While brick-and-mortar stores possess rich inventory, customer orders frequently fail due to stock-outs during peak picking hours, rigid delivery schedules, and poor handling of unavailable items. When an ordered brand of milk or rice is missing from the shelf, customer orders are either cancelled or arbitrarily replaced with unwanted items, leading to high return rates and customer frustration.

To solve this, FreshCart requires an online grocery ordering platform featuring:
1. **Guaranteed Delivery Slots:** Time-windowed delivery slots with real-time capacity management.
2. **Intelligent Substitution Logic:** An automated engine that detects out-of-stock items and recommends category-matched, price-capped alternatives while respecting customer allergen and dietary filters.
3. **Explicit Customer Consent:** Giving customers complete authority to accept or reject suggested replacements prior to dispatch.

---

## 2. Process Model Justification: Why the Incremental Model?

The software engineering process model assigned to Case 37 is the **Incremental Model**. 

### 2.1 Evaluation Against Project Characteristics

```
+-----------------------------------------------------------------------------------+
|                            Incremental Lifecycle Model                            |
+-----------------------------------------------------------------------------------+
|  Increment 1: Core Foundation   --> Catalog, Shopping Basket, SQLite DB, Basic UI  |
|  Increment 2: Core Prototype    --> Substitution Logic, Out-of-Stock Detection     |
|  Increment 3: Delivery Engine   --> Slot Booking, Capacity Limits, Checkout Flow   |
|  Increment 4: Operations & Mon. --> Health Endpoint, Order Tracking, Audit Logs    |
+-----------------------------------------------------------------------------------+
```

1. **Early Business Value:** Rather than waiting for a full-scale enterprise ERP, the grocery chain can launch **Increment 1** with basic ordering and in-store pickup within 2 weeks.
2. **Controlled Complexity for the Prototype Module:** The primary technical novelty lies in the **Substitution Logic**. Isolating this into **Increment 2** allows extensive unit testing, allergen safety validation, and boundary verification without risking base catalog stability.
3. **Operational Feedback Loop:** In-store store-staff and pickers interact with each usable increment, refining picking ergonomics before delivery slot automation (Increment 3) is deployed.
4. **Risk Mitigation:** If the AI substitution model suggests an inappropriate item, only the substitution service is refined without taking down catalog browsing or order placement.

---

## 3. Raw Store-Staff Chat Message Elicitation

During field observations, informal chat messages from store managers, inventory stockers, and order pickers were gathered via store WhatsApp/Slack communication channels:

> **Picker Ramesh (08:14 AM):** *"A customer ordered Amul Taaza 1L, but our fridge only has Nandini Toned Milk and Full Cream. Which one do I pack? If I pack Nandini, customer says price is less and bill doesn't match!"*  
> **Manager Deepa (08:17 AM):** *"Never pack another item without customer approval! Show them the alternative on their screen and let them click Accept or Reject. Also make sure the price doesn't jump more than 15-20%."*  
> **Picker Suresh (11:30 AM):** *"Evening slots between 5 PM and 7 PM are always overloaded. Delivery boys can only carry 10 crates per hour. Stop taking orders when the 5-7 PM slot reaches 10!"*  
> **Stock Incharge Anand (02:15 PM):** *"People with nut allergies get very angry if plant milk with almonds is offered as dairy milk substitute. Check allergens before showing replacements."*  
> **Dispatcher Priya (06:00 PM):** *"We need a health monitor. Sometimes the backend disconnects during checkout and pickers are left waiting."*

---

## 4. ChatGPT Requirements Parsing and Human Validation

ChatGPT was utilized to parse the unstructured chat messages into formal Functional Requirements (FR) and Non-Functional Requirements (NFR). A senior software engineering review was applied to eliminate ambiguities, enforce measurable acceptance criteria, and establish traceability.

| Req ID | Raw Chat Origin | AI-Drafted Requirement | Human Engineering Validation & Testable Criteria | Priority |
| :--- | :--- | :--- | :--- | :---: |
| **FR-01** | Picker Suresh (Slot overload) | System must allow customer to select delivery slot. | **Refined:** The customer shall select an available delivery slot during checkout. The system shall dynamically disable slots whose capacity limit (10 orders/slot) is reached. | **Must Have** |
| **FR-02** | Picker Ramesh & Manager Deepa | System suggests an alternative when item is out of stock. | **Refined:** When an ordered SKU has `in_stock = False` or `stock_qty < cart_qty`, the system shall automatically recommend in-stock candidates from the same category where price delta $\le 20\%$. | **Must Have** |
| **FR-03** | Manager Deepa (Approval) | Customer can accept or reject substitute. | **Refined:** The UI shall display a side-by-side comparison. Clicking 'Accept' shall swap the cart SKU; clicking 'Reject' shall remove the unavailable item without blocking order checkout. | **Must Have** |
| **FR-04** | Stock Incharge Anand | Filter out allergens. | **Refined:** The substitution engine shall cross-reference customer allergen tags (`avoid_allergens`) against candidate allergen metadata and exclude all intersecting items. | **Must Have** |
| **FR-05** | Dispatcher Priya | Monitor system status. | **Refined:** The application shall expose a `/health` endpoint returning HTTP 200 with JSON payload (`status`, `database`, `timestamp`) with response latency $< 500\text{ ms}$. | **Should Have** |
| **NFR-01** | Performance & Throughput | System should be fast. | **Refined:** The substitution recommendation algorithm shall compute and return top 3 ranked candidates in $< 50\text{ ms}$ for a catalog of up to 5,000 SKUs. | **High** |
| **NFR-02** | Stock Integrity & Concurrency | Stock updates must be reliable. | **Refined:** Inventory decrements and slot bookings shall execute within an ACID-compliant SQLite transaction to prevent overselling. | **High** |

---

## 5. Architectural & Incremental Delivery Roadmap

```
+------------------------------------------------------------------------------------+
| Increment 1 (Days 1–7): Baseline E-Commerce                                       |
| - Product catalog, category filtering, SQLite schema, shopping cart session.       |
+------------------------------------------------------------------------------------+
| Increment 2 (Days 8–14): Substitution Engine Prototype                            |
| - Rule engine, allergen avoidance, price threshold logic, PyTest unit test suite.  |
+------------------------------------------------------------------------------------+
| Increment 3 (Days 15–21): Slot Booking & Checkout Workflow                         |
| - Delivery slot reservation, capacity enforcement, order confirmation, Selenium.  |
+------------------------------------------------------------------------------------+
| Increment 4 (Days 22–28): Quality Assurance, DevOps & Health Monitoring            |
| - Docker containerization, Jenkins pipeline, SonarQube audit, /health probe.       |
+------------------------------------------------------------------------------------+
```

Evidence attached: Visual SDLC process flow diagram at [screenshots/incremental_sdlc.png](file:///e:/Case37-Online-Grocery/screenshots/incremental_sdlc.png).
