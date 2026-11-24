# Lab Experiment L2.3 — Epic Decomposition: One Epic and Five User Stories with Acceptance Criteria

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Agile Framework:** Kanban | **Tool:** ChatGPT  

---

## 1. Aim
To decompose a major grocery fulfillment Epic into 5 distinct, INVEST-compliant User Stories (US-01 to US-05) complete with formal Given-When-Then acceptance criteria.

---

## 2. Epic Definition
**Epic EP-01: Intelligent Grocery Substitution & Slot-Constrained Delivery Engine**  
*As an online grocery shopper, I want the system to reserve guaranteed delivery time windows and intelligently suggest safe, price-capped alternatives when my requested items are unavailable, so that my household grocery needs are fulfilled reliably and transparently.*

---

## 3. Five Detailed User Stories

### US-01: Delivery Slot Reservation with Capacity Enforcement
- **User Story:** *As an online grocery customer, I want to select a guaranteed 2-hour delivery slot during checkout, so that I receive my groceries when I am available at home.*
- **Priority:** High | **Story Points:** 3
- **Acceptance Criteria (Gherkin):**
  - **Scenario 1 (Slot Available):** *Given* a delivery slot has fewer than 10 booked orders, *When* the customer reaches checkout, *Then* the slot radio button is enabled and displays available seats.
  - **Scenario 2 (Slot Full):** *Given* a delivery slot has reached 10 booked orders, *When* the customer views slots, *Then* the slot is disabled with a red `[FULL]` badge and cannot be selected.

### US-02: Real-Time Inventory & Out-of-Stock Detection
- **User Story:** *As an online grocery customer, I want the shopping cart to detect out-of-stock items before payment, so that I am never charged for goods that cannot be picked from shelves.*
- **Priority:** High | **Story Points:** 5
- **Acceptance Criteria (Gherkin):**
  - **Scenario 1:** *Given* an item in the cart has `in_stock = False` or `stock_qty < cart_qty`, *When* the customer views the cart, *Then* an amber alert banner displays *"Unavailable Items Detected in Basket!"* and prompts for substitution review.

### US-03: Intelligent Category and Price-Capped Substitution
- **User Story:** *As an online grocery customer, I want the system to automatically recommend in-stock alternatives from the same category within a 20% price increase, so that I get comparable groceries at fair prices.*
- **Priority:** High | **Story Points:** 5
- **Acceptance Criteria (Gherkin):**
  - **Scenario 1:** *Given* an item is out of stock, *When* the substitution engine evaluates replacements, *Then* only candidates matching the exact category and priced $\le \text{Base Price} \times 1.20$ are recommended.

### US-04: Explicit Customer Substitution Decisioning (Accept/Reject)
- **User Story:** *As an online grocery customer, I want the ability to explicitly accept or reject any suggested substitute, so that store staff never replace items without my permission.*
- **Priority:** High | **Story Points:** 3
- **Acceptance Criteria (Gherkin):**
  - **Scenario 1 (Accept):** *Given* a suggested replacement, *When* the customer clicks *Accept*, *Then* the unavailable SKU is swapped with the substitute SKU in the cart and price total is recalculated.
  - **Scenario 2 (Reject):** *Given* a suggested replacement, *When* the customer clicks *Reject*, *Then* the unavailable item is removed from the cart and the customer can proceed with remaining items.

### US-05: Order Confirmation & Continuous Health API
- **User Story:** *As a store manager, I want a persistent order record and a continuous `/health` endpoint, so that operations can track order fulfillment status and monitor backend uptime.*
- **Priority:** Medium | **Story Points:** 3
- **Acceptance Criteria (Gherkin):**
  - **Scenario 1:** *Given* a placed order, *When* `/order/confirmation/<code>` is rendered, *Then* all fulfilled SKUs, substitution audit notes, and delivery slots are displayed.
  - **Scenario 2:** *Given* an active server, *When* `GET /health` is requested, *Then* HTTP 200 is returned with JSON payload `{"status": "healthy", "database": "UP"}`.
