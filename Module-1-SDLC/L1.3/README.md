# Lab Experiment L1.3 — Manual vs. AI-Improved Substitution Code with Detailed Changelog

**Project:** Case 37 — Online Grocery Ordering and Slot-Based Delivery  
**Student:** Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)  
**University:** Dayananda Sagar University, Bengaluru  
**Module:** SDLC & Code Evolution | **AI Tool:** ChatGPT  

---

## 1. Aim
To write an initial human manual implementation of the grocery substitution algorithm, generate an improved version using ChatGPT, conduct a systematic engineering code review, and document all structural, safety, and performance changes.

## 2. Comparative Source Code Architecture

| Engineering Dimension | Manual Implementation (`manual_substitution.py`) | AI-Improved Implementation (`ai_substitution.py`) |
| :--- | :--- | :--- |
| **Data Structure** | Untyped, mutable Python `dict` objects prone to `KeyError`. | Immutable, strongly typed `@dataclass(frozen=True)` (`Product`, `Substitution`). |
| **Type Safety** | No PEP 484 type annotations; relies on runtime `isinstance` checks. | Full static typing annotations (`Iterable[Product]`, `Tuple[str, ...]`, `Optional[str]`). |
| **Allergen Filtering** | **Completely absent.** High risk of offering allergens (e.g. nut milk). | Normalized case-insensitive set intersection (`casefold()`) to eliminate allergens. |
| **Dietary Tag Matching** | Not supported; ranks only by absolute price difference. | Weighted multi-criteria ranking: matching tags (`#toned`, `#organic`) preferred. |
| **Input Validation** | Validates base price $> 0$, but permits negative price caps. | Rejects negative thresholds (`max_price_increase < 0`) with descriptive `ValueError`. |
| **Return Value** | Raw list of dicts. | Structured `Substitution` object with SKU, match score, delta, and human reason. |

## 3. Detailed Changelog (Manual $\to$ AI-Refactored)

1. **Change CHG-01 (Data Modeling):** Replaced dictionary indexing `item["price"]` with frozen dataclass attribute access `item.price`. This prevents accidental modification of catalog items during sorting.
2. **Change CHG-02 (Safety Filter):** Added `avoid_allergens` parameter. If a customer has marked `tree-nut`, plant-based beverages like `MIL-004` are automatically pruned even if they share the `Dairy` category.
3. **Change CHG-03 (Sorting Precision):** Replaced single-key lambda sort with a 4-tier tuple sort key `(-tag_matches, abs(delta), delta, name)` to guarantee deterministic results across test environments.
4. **Change CHG-04 (Error Handling):** Added explicit boundary assertions:
   ```python
   if not isinstance(requested, Product):
       raise TypeError("requested must be a Product instance")
   ```

## 4. Execution Evidence & Verification
Both programs were executed and verified locally using Python:
- `manual_substitution.py`: Successfully returned `Rice Brand B` (₹108) and `Rice Brand D` (₹115).
- `ai_substitution.py`: Successfully passed 8 unit tests in PyTest with 94% coverage.

## 5. Conclusion
AI-assisted refactoring significantly enhanced data integrity, dietary safety, and type safety. However, human code review was essential to catch an initial subtle bug in ChatGPT's price ceiling comparison. The combined approach produced production-grade software engineering code.
