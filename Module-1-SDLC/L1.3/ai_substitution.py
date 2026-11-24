"""AI-improved version of substitution logic refactored with Python dataclasses and allergen safety.

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
Refactored using ChatGPT with strict human engineering constraints.
"""

from dataclasses import dataclass
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


@dataclass(frozen=True)
class Substitution:
    requested_sku: str
    selected_sku: Optional[str]
    reason: str
    price_difference: float = 0.0
    selected_product: Optional[Product] = None
    match_score: float = 1.0


def suggest_substitution_ai(
    requested: Product,
    catalog: Iterable[Product],
    *,
    avoid_allergens: Tuple[str, ...] = (),
    max_price_increase: float = 0.0,
    max_price_percent: float = 0.20,
    preferred_tags: Tuple[str, ...] = ()
) -> Substitution:
    """Robust, type-safe, allergen-aware substitution engine."""
    if not isinstance(requested, Product):
        raise TypeError("requested must be a Product instance")
    if max_price_increase < 0 or max_price_percent < 0:
        raise ValueError("Price thresholds cannot be negative")

    if requested.in_stock and requested.stock_qty > 0:
        return Substitution(requested.sku, requested.sku, "Requested item is in stock", 0.0, requested, 1.0)

    blocked = {a.strip().casefold() for a in avoid_allergens if a.strip()}
    preferred = {t.strip().casefold() for t in preferred_tags if t.strip()}
    max_delta = max_price_increase if max_price_increase > 0 else round(requested.price * max_price_percent, 2)

    candidates = []
    for item in catalog:
        if not isinstance(item, Product) or item.sku == requested.sku:
            continue
        if not item.in_stock or item.stock_qty <= 0:
            continue
        if item.category.strip().casefold() != requested.category.strip().casefold():
            continue
        if item.price <= 0:
            continue
        if blocked.intersection(a.strip().casefold() for a in item.allergens):
            continue
        delta = round(item.price - requested.price, 2)
        if delta > max_delta:
            continue

        item_tags = {t.strip().casefold() for t in item.tags}
        tag_matches = len(preferred.intersection(item_tags))
        candidates.append((-tag_matches, abs(delta), delta, item.name.casefold(), item, delta))

    if not candidates:
        return Substitution(requested.sku, None, "No safe eligible substitute found", 0.0, None, 0.0)

    candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    chosen, delta = candidates[0][4], candidates[0][5]
    score = max(0.5, min(1.0, round(1.0 - (abs(delta) / (requested.price + 0.001)), 2)))

    return Substitution(requested.sku, chosen.sku, f"Recommended: {chosen.name} (Δ ₹{delta:+.2f})", delta, chosen, score)
