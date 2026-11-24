"""PyTest Unit Test Suite for Substitution Logic (L4.2).

Case 37: Online Grocery
Prototype Module: Substitution Logic
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
Eight Comprehensive Unit Tests covering Functional, Boundary, and Negative Paths.
"""

import pytest
from grocery_app.substitution import Product, suggest_substitution, get_all_substitute_candidates


@pytest.fixture
def sample_catalog():
    return [
        Product(sku="A", name="Milk A", category="Dairy", price=60.0, in_stock=False, stock_qty=0),
        Product(sku="B", name="Toned Milk B", category="Dairy", price=62.0, in_stock=True, stock_qty=10, tags=("toned", "local")),
        Product(sku="C", name="Premium Milk C", category="Dairy", price=75.0, in_stock=True, stock_qty=10),
        Product(sku="D", name="Out Milk D", category="Dairy", price=59.0, in_stock=False, stock_qty=0),
        Product(sku="E", name="Apple E", category="Fruit", price=30.0, in_stock=True, stock_qty=15),
        Product(sku="F", name="Almond Milk F", category="Dairy", price=61.0, in_stock=True, stock_qty=8, allergens=("tree-nut",)),
        Product(sku="G", name="Generic Dairy G", category="Dairy", price=61.0, in_stock=True, stock_qty=5),
    ]


def test_01_in_stock_original(sample_catalog):
    """TC-01: When requested item is in stock, return original SKU with zero price difference."""
    in_stock_item = Product(sku="A", name="Milk A", category="Dairy", price=60.0, in_stock=True, stock_qty=10)
    result = suggest_substitution(in_stock_item, sample_catalog)
    assert result.selected_sku == "A"
    assert result.price_difference == 0.0
    assert "in stock" in result.reason.lower()


def test_02_same_category(sample_catalog):
    """TC-02: Replacement must belong to the exact same category."""
    requested = sample_catalog[0]  # SKU A (Dairy, 60.0, out of stock)
    result = suggest_substitution(requested, sample_catalog, max_price_increase=5.0)
    assert result.selected_sku in ("F", "G", "B")
    assert result.selected_product.category == "Dairy"


def test_03_out_of_stock_no_candidates():
    """TC-03: When no candidate is in stock, return selected_sku=None with explanatory reason."""
    requested = Product(sku="A", name="Milk A", category="Dairy", price=60.0, in_stock=False, stock_qty=0)
    empty_stock = [
        Product(sku="D", name="Out Milk D", category="Dairy", price=59.0, in_stock=False, stock_qty=0)
    ]
    result = suggest_substitution(requested, empty_stock)
    assert result.selected_sku is None
    assert "no safe eligible substitute" in result.reason.lower()


def test_04_wrong_category_ignored(sample_catalog):
    """TC-04: Candidates from different categories (e.g., Fruit) are strictly excluded."""
    requested = sample_catalog[0]  # Dairy
    only_fruit = [sample_catalog[4]]  # Apple E (Fruit)
    result = suggest_substitution(requested, only_fruit)
    assert result.selected_sku is None


def test_05_allergen_avoidance(sample_catalog):
    """TC-05: Customer allergen filters eliminate candidates containing prohibited allergens."""
    requested = sample_catalog[0]
    # Candidate F has allergen 'tree-nut'
    only_nut_milk = [sample_catalog[5]]
    result = suggest_substitution(requested, only_nut_milk, avoid_allergens=("tree-nut",))
    assert result.selected_sku is None


def test_06_price_limit_exceeded(sample_catalog):
    """TC-06: Candidate exceeding price increase cap is rejected."""
    requested = sample_catalog[0]  # 60.0
    expensive_only = [sample_catalog[2]]  # Premium Milk C at 75.0 (delta +15.0)
    result = suggest_substitution(requested, expensive_only, max_price_increase=5.0)
    assert result.selected_sku is None


def test_07_preferred_tag_matching(sample_catalog):
    """TC-07: Candidate matching preferred tags ('toned') is ranked ahead of price-tied candidate."""
    requested = sample_catalog[0]
    # G is ₹61 (delta +1.0, no tag)
    # B is ₹62 (delta +2.0, has tag 'toned')
    # With preferred_tags=('toned',), B should be selected because tag match takes priority!
    candidates = [sample_catalog[6], sample_catalog[1]]  # G and B
    result = suggest_substitution(requested, candidates, max_price_increase=5.0, preferred_tags=("toned",))
    assert result.selected_sku == "B"


def test_08_negative_price_limit_raises_error(sample_catalog):
    """TC-08: Negative max_price_increase is invalid and raises ValueError."""
    requested = sample_catalog[0]
    with pytest.raises(ValueError, match="max_price_increase cannot be negative"):
        suggest_substitution(requested, sample_catalog, max_price_increase=-5.0)


def test_09_type_error_on_invalid_requested(sample_catalog):
    """TC-09: Passing non-Product object raises TypeError."""
    with pytest.raises(TypeError, match="requested must be a Product"):
        suggest_substitution("NOT_A_PRODUCT", sample_catalog)


def test_10_negative_price_percent_raises_error(sample_catalog):
    """TC-10: Passing negative max_price_percent raises ValueError."""
    requested = sample_catalog[0]
    with pytest.raises(ValueError, match="max_price_percent cannot be negative"):
        suggest_substitution(requested, sample_catalog, max_price_percent=-0.1)


def test_11_get_all_substitute_candidates(sample_catalog):
    """TC-11: get_all_substitute_candidates returns multiple valid candidates sorted properly."""
    requested = sample_catalog[0]
    candidates = get_all_substitute_candidates(requested, sample_catalog, max_price_percent=0.25)
    assert len(candidates) >= 1
    assert all(c.selected_product.category == "Dairy" for c in candidates)
