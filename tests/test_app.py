"""Integration Test Suite for FreshCart Online Grocery Web Application.

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

import pytest
from grocery_app.app import app
from grocery_app.database import init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-secret-key-case-37"
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client


def test_int_01_health_check_endpoint(client):
    """Verify continuous monitoring health endpoint returns 200 OK and valid JSON."""
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "healthy"
    assert data["database"] == "UP"
    assert data["case_number"] == 37
    assert data["prototype_module"] == "Substitution Logic"


def test_int_02_catalog_display(client):
    """Verify catalogue returns 200 and contains grocery sections."""
    res = client.get("/")
    assert res.status_code == 200
    assert b"FreshCart" in res.data
    assert b"Dairy" in res.data
    assert b"Nandini Toned Fresh Milk" in res.data


def test_int_03_search_functionality(client):
    """Verify search filter for 'milk' returns milk products."""
    res = client.get("/?q=milk")
    assert res.status_code == 200
    assert b"Milk" in res.data


def test_int_04_add_out_of_stock_item_and_review(client):
    """Verify adding an out-of-stock item triggers substitution alert."""
    # MIL-002 is out of stock (Amul Taaza Milk)
    res = client.post("/cart/add", data={"sku": "MIL-002", "quantity": 1}, follow_redirects=True)
    assert res.status_code == 200
    assert b"OUT OF STOCK" in res.data

    # Review substitutions page
    sub_res = client.get("/substitutions")
    assert sub_res.status_code == 200
    assert b"Amul Taaza Homogenised Milk" in sub_res.data
    assert b"Nandini Toned Fresh Milk" in sub_res.data


def test_int_05_accept_substitution_flow(client):
    """Verify accepting a substitution replaces the unavailable SKU with substitute SKU."""
    client.post("/cart/add", data={"sku": "MIL-002", "quantity": 1}, follow_redirects=True)
    res = client.post("/substitutions/action", data={
        "original_sku": "MIL-002",
        "substitute_sku": "MIL-001",
        "action": "accept"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Substitution accepted" in res.data


def test_int_06_reject_substitution_flow(client):
    """Verify rejecting a substitution removes unavailable item."""
    client.post("/cart/add", data={"sku": "BUT-001", "quantity": 1}, follow_redirects=True)
    res = client.post("/substitutions/action", data={
        "original_sku": "BUT-001",
        "action": "reject"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Substitution rejected" in res.data


def test_int_07_full_order_placement(client):
    """Verify end-to-end order placement with slot selection."""
    # Add in-stock item
    client.post("/cart/add", data={"sku": "MIL-001", "quantity": 2}, follow_redirects=True)
    
    # Place order with valid slot
    order_data = {
        "customer_name": "Likhith Gowda",
        "phone": "9876543210",
        "address": "No. 37, 5th Main, Kumaraswamy Layout, Bengaluru",
        "slot_id": "1",
        "dietary_preference": "Standard",
    }
    res = client.post("/order/place", data=order_data, follow_redirects=True)
    assert res.status_code == 200
    assert b"Order Confirmed" in res.data
    assert b"Likhith Gowda" in res.data


def test_int_08_api_catalog_and_substitute_endpoints(client):
    """Verify REST API endpoints for catalog and substitution."""
    res = client.get("/api/catalog")
    assert res.status_code == 200
    catalog = res.get_json()
    assert len(catalog) > 0

    sub_res = client.post("/api/substitute", json={
        "sku": "MIL-002",
        "avoid_allergens": [],
        "max_price_increase": 10.0
    })
    assert sub_res.status_code == 200
    data = sub_res.get_json()
    assert data["selected_sku"] == "MIL-001"
    assert data["match_score"] > 0


def test_int_09_product_detail_page(client):
    """Verify product detail view for both in-stock and out-of-stock items."""
    res = client.get("/product/MIL-001")
    assert res.status_code == 200
    assert b"Nandini Toned Fresh Milk" in res.data

    # Out of stock item should show substitution suggestions
    res_oos = client.get("/product/MIL-002")
    assert res_oos.status_code == 200
    assert b"Out of Stock" in res_oos.data


def test_int_10_checkout_input_validation_errors(client):
    """Verify checkout form validates short name, invalid phone, and missing address."""
    client.post("/cart/add", data={"sku": "MIL-001", "quantity": 1}, follow_redirects=True)

    # Invalid phone
    bad_phone_res = client.post("/order/place", data={
        "customer_name": "Likhith",
        "phone": "123",  # Invalid phone
        "address": "Valid delivery address in Bengaluru",
        "slot_id": "1",
    }, follow_redirects=True)
    assert b"Please enter a valid 10-digit" in bad_phone_res.data
