"""Substitution Logic Engine for Online Grocery Application.

Case 37: Online Grocery
Prototype Module: Substitution Logic
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    category: str
    price: float
    in_stock: bool
    stock_qty: int = 10
    allergens: Tuple[str, ...] = ()
    tags: Tuple[str, ...] = ()
    unit: str = "1 unit"
    description: str = ""


@dataclass(frozen=True)
class Substitution:
    requested_sku: str
    selected_sku: Optional[str]
    reason: str
    price_difference: float = 0.0
    selected_product: Optional[Product] = None
    match_score: float = 1.0


def suggest_substitution(
    requested: Product,
    catalog: Iterable[Product],
    *,
    avoid_allergens: Tuple[str, ...] = (),
    max_price_increase: float = 0.0,
    max_price_percent: float = 0.20,
    preferred_tags: Tuple[str, ...] = ()
) -> Substitution:
    """Select a safe, in-stock, same-category replacement under customer rules.

    Rules:
    1. Category must match exactly (case-insensitive).
    2. Candidate must be currently in stock (in_stock is True and stock_qty > 0).
    3. Candidate must NOT contain any allergen from customer's avoid_allergens list.
    4. Candidate price must be positive (> 0).
    5. Price increase must not exceed max_price_increase (if specified > 0)
       or (requested.price * max_price_percent).
    6. Candidates are ranked by:
       - Highest number of matching preferred tags.
       - Smallest absolute price difference.
       - Lower price in case of tie.
       - Alphabetical name.
    """
    if not isinstance(requested, Product):
        raise TypeError("requested must be a Product instance")
    if max_price_increase < 0:
        raise ValueError("max_price_increase cannot be negative")
    if max_price_percent < 0:
        raise ValueError("max_price_percent cannot be negative")

    # If requested item is in stock with available inventory, return it directly
    if requested.in_stock and requested.stock_qty > 0:
        return Substitution(
            requested_sku=requested.sku,
            selected_sku=requested.sku,
            reason="Requested item is in stock",
            price_difference=0.0,
            selected_product=requested,
            match_score=1.0,
        )

    blocked_allergens = {a.strip().casefold() for a in avoid_allergens if a.strip()}
    preferred = {t.strip().casefold() for t in preferred_tags if t.strip()}

    effective_max_delta = (
        max_price_increase
        if max_price_increase > 0
        else round(requested.price * max_price_percent, 2)
    )

    candidates: List[Tuple[int, float, float, str, Product, float]] = []

    for item in catalog:
        if not isinstance(item, Product):
            continue
        # Skip the original requested SKU
        if item.sku == requested.sku:
            continue
        # Candidate must be in stock
        if not item.in_stock or item.stock_qty <= 0:
            continue
        # Category match check
        if item.category.strip().casefold() != requested.category.strip().casefold():
            continue
        # Price must be valid positive number
        if item.price <= 0:
            continue
        # Allergen safety check
        item_allergens = {a.strip().casefold() for a in item.allergens}
        if blocked_allergens.intersection(item_allergens):
            continue
        # Price cap check
        delta = round(item.price - requested.price, 2)
        if delta > effective_max_delta:
            continue

        # Preference matching
        item_tags = {t.strip().casefold() for t in item.tags}
        matching_tags_count = len(preferred.intersection(item_tags))

        # Tuple structure for sorting: (-tag_matches, abs(delta), delta, name, item, delta)
        candidates.append(
            (-matching_tags_count, abs(delta), delta, item.name.casefold(), item, delta)
        )

    if not candidates:
        return Substitution(
            requested_sku=requested.sku,
            selected_sku=None,
            reason="No safe eligible substitute found in stock meeting price and dietary criteria",
            price_difference=0.0,
            selected_product=None,
            match_score=0.0,
        )

    candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    chosen_product = candidates[0][4]
    chosen_delta = candidates[0][5]
    match_score = round(1.0 - (abs(chosen_delta) / (requested.price + 0.001)), 2)
    match_score = max(0.5, min(1.0, match_score))

    return Substitution(
        requested_sku=requested.sku,
        selected_sku=chosen_product.sku,
        reason=f"Recommended substitution: {chosen_product.name} (Δ ₹{chosen_delta:+.2f})",
        price_difference=chosen_delta,
        selected_product=chosen_product,
        match_score=match_score,
    )


def get_all_substitute_candidates(
    requested: Product,
    catalog: Iterable[Product],
    *,
    avoid_allergens: Tuple[str, ...] = (),
    max_price_percent: float = 0.25,
    preferred_tags: Tuple[str, ...] = ()
) -> List[Substitution]:
    """Return all valid substitute alternatives ranked by suitability."""
    if not isinstance(requested, Product):
        raise TypeError("requested must be a Product instance")

    blocked_allergens = {a.strip().casefold() for a in avoid_allergens if a.strip()}
    preferred = {t.strip().casefold() for t in preferred_tags if t.strip()}
    effective_max_delta = round(requested.price * max_price_percent, 2)

    results: List[Substitution] = []
    candidates: List[Tuple[int, float, float, str, Product, float]] = []

    for item in catalog:
        if not isinstance(item, Product) or item.sku == requested.sku:
            continue
        if not item.in_stock or item.stock_qty <= 0:
            continue
        if item.category.strip().casefold() != requested.category.strip().casefold():
            continue
        if item.price <= 0:
            continue
        item_allergens = {a.strip().casefold() for a in item.allergens}
        if blocked_allergens.intersection(item_allergens):
            continue
        delta = round(item.price - requested.price, 2)
        if delta > effective_max_delta:
            continue

        item_tags = {t.strip().casefold() for t in item.tags}
        matching_tags_count = len(preferred.intersection(item_tags))
        candidates.append(
            (-matching_tags_count, abs(delta), delta, item.name.casefold(), item, delta)
        )

    candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    for c in candidates:
        prod = c[4]
        delta = c[5]
        score = max(0.5, min(1.0, round(1.0 - (abs(delta) / (requested.price + 0.001)), 2)))
        results.append(
            Substitution(
                requested_sku=requested.sku,
                selected_sku=prod.sku,
                reason=f"Alternative in {prod.category} (Δ ₹{delta:+.2f})",
                price_difference=delta,
                selected_product=prod,
                match_score=score,
            )
        )
    return results

