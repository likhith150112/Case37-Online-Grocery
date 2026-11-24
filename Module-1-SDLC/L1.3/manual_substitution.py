"""Manual initial version of substitution logic written by engineering student.

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

def suggest_substitutes(item, candidates, max_increase=0.20):
    """Initial manual implementation using untyped dictionaries."""
    if not isinstance(item, dict):
        return []
    base = item.get("price")
    category = item.get("category")
    if not isinstance(base, (int, float)) or base <= 0 or not category:
        return []
    limit = base * (1 + max_increase)
    valid = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        price = candidate.get("price")
        # Check matching category, positive price, and price ceiling
        if (candidate.get("category") == category and
            isinstance(price, (int, float)) and
            0 < price <= limit):
            valid.append(candidate)

    # Sort by absolute price proximity
    return sorted(valid, key=lambda c: (abs(c["price"] - base), c["price"]))


if __name__ == "__main__":
    unavailable = {"name": "Rice Brand A", "category": "rice", "price": 100}
    stock = [
        {"name": "Rice Brand B", "category": "rice", "price": 108},
        {"name": "Rice Brand C", "category": "rice", "price": 125},
        {"name": "Cooking Oil", "category": "oil", "price": 90},
        {"name": "Rice Brand D", "category": "rice", "price": 115},
    ]
    print("Manual Substitution Prototype:")
    print("Unavailable:", unavailable["name"])
    print("Suggestions:")
    for s in suggest_substitutes(unavailable, stock):
        print("-", s["name"], "₹" + str(s["price"]))
