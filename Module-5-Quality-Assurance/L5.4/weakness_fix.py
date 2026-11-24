"""Demonstration of Identifying, Fixing, and Verifying a Deliberate AI Weakness (L5.4).

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
Weakness: AI substitution code accepted negative prices (e.g. -₹50.00) because it only checked
whether price was below maximum threshold.
Fix: Added strict positive price validation (candidate.price > 0).
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    category: str
    price: float
    in_stock: bool


# -------------------------------------------------------------
# 1. FLAWED AI IMPLEMENTATION (Contains Subtle Vulnerability)
# -------------------------------------------------------------
def flawed_ai_suggest_substitute(requested: Product, candidates: List[Product], max_price_increase=0.20):
    """FLAWED: Checks only if price <= limit, allowing negative prices through!"""
    limit = requested.price * (1 + max_price_increase)
    valid = []
    for item in candidates:
        if item.category == requested.category and item.in_stock:
            # BUG: Misses check for item.price > 0
            if item.price <= limit:
                valid.append(item)
    return valid[0] if valid else None


# -------------------------------------------------------------
# 2. FIXED SECURE IMPLEMENTATION (Human Engineering Fix)
# -------------------------------------------------------------
def fixed_suggest_substitute(requested: Product, candidates: List[Product], max_price_increase=0.20):
    """SECURE: Validates positive price, matching category, and stock."""
    if not isinstance(requested, Product):
        raise TypeError("requested must be a Product instance")
    if requested.price <= 0:
        raise ValueError("requested price must be positive")

    limit = round(requested.price * (1 + max_price_increase), 2)
    valid = []
    for item in candidates:
        if not isinstance(item, Product) or not item.in_stock:
            continue
        if item.category.casefold() != requested.category.casefold():
            continue
        # THE FIX: Require strictly positive price
        if item.price <= 0:
            continue
        if item.price <= limit:
            valid.append(item)

    if not valid:
        return None
    valid.sort(key=lambda x: (abs(x.price - requested.price), x.price))
    return valid[0]


# -------------------------------------------------------------
# 3. VERIFICATION TESTS
# -------------------------------------------------------------
if __name__ == "__main__":
    print("=== L5.4 Deliberate AI Weakness Discovery & Verification ===")

    requested_milk = Product("MIL-001", "Toned Milk 1L", "Dairy", 50.0, False)

    # Catalog containing a corrupt inventory item with negative price (-₹10.00)
    test_catalog = [
        Product("GLITCH-001", "Corrupt Glitch Item", "Dairy", -10.0, True),
        Product("MIL-002", "Fresh Milk Alternate", "Dairy", 54.0, True),
    ]

    print("\n[Step 1] Testing Flawed AI Code:")
    flawed_result = flawed_ai_suggest_substitute(requested_milk, test_catalog)
    print(f"Flawed AI chose: {flawed_result.name} at ₹{flawed_result.price}")
    if flawed_result.price < 0:
        print("--> CRITICAL VULNERABILITY CONFIRMED: Negative price item was selected as valid substitute!")

    print("\n[Step 2] Testing Fixed Human Engineering Code:")
    fixed_result = fixed_suggest_substitute(requested_milk, test_catalog)
    print(f"Fixed Code chose: {fixed_result.name} at ₹{fixed_result.price}")
    assert fixed_result.price > 0, "Price must be strictly positive"
    assert fixed_result.sku == "MIL-002", "Must pick genuine valid product"
    print("--> VERIFICATION PASSED: Glitch item successfully rejected. Legitimate product selected.")
