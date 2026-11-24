"""FreshCart - Online Grocery Web Application
Case 37: Online Grocery
Prototype Module: Substitution Logic
Agile: Kanban | Process Model: Incremental | AI Tool: ChatGPT
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

import datetime
import os
import secrets
import sqlite3
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from grocery_app.database import (
    get_db_connection,
    get_delivery_slots,
    get_product,
    init_db,
    load_catalog_from_db,
)
from grocery_app.substitution import (
    Product,
    get_all_substitute_candidates,
    suggest_substitution,
)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(16))

# Ensure database is initialized on startup
with app.app_context():
    init_db()


@app.context_processor
def inject_global_vars():
    """Inject cart count and global metadata into templates."""
    cart = session.get("cart", {})
    cart_count = sum(cart.values())
    return {
        "cart_count": cart_count,
        "student_name": "Likhith Gowda M S",
        "student_usn": "ENG24CS0105",
        "roll_no": 37,
        "case_no": 37,
    }


# ==========================================
# CATALOG & BROWSING ROUTES
# ==========================================

@app.route("/")
def index():
    """Main catalog page with search and category filtering."""
    catalog = load_catalog_from_db()
    search_query = request.args.get("q", "").strip()
    category_filter = request.args.get("category", "").strip()

    categories = sorted(list({p.category for p in catalog}))

    filtered_catalog = catalog
    if category_filter:
        filtered_catalog = [
            p for p in filtered_catalog if p.category.casefold() == category_filter.casefold()
        ]
    if search_query:
        q = search_query.casefold()
        filtered_catalog = [
            p for p in filtered_catalog
            if q in p.name.casefold() or q in p.description.casefold() or any(q in t for t in p.tags)
        ]

    return render_template(
        "index.html",
        products=filtered_catalog,
        categories=categories,
        current_category=category_filter,
        search_query=search_query,
    )


@app.route("/product/<sku>")
def product_detail(sku):
    """Product detail page with stock status and substitution preview."""
    product = get_product(sku)
    if not product:
        flash(f"Product {sku} not found.", "warning")
        return redirect(url_for("index"))

    catalog = load_catalog_from_db()
    substitutes = []
    if not product.in_stock:
        substitutes = get_all_substitute_candidates(product, catalog)

    return render_template(
        "product_detail.html",
        product=product,
        substitutes=substitutes,
    )


# ==========================================
# CART MANAGEMENT
# ==========================================

@app.route("/cart")
def view_cart():
    """View shopping cart with out-of-stock detection and substitution banner."""
    cart = session.get("cart", {})
    catalog = load_catalog_from_db()
    catalog_map = {p.sku: p for p in catalog}

    cart_items = []
    subtotal = 0.0
    has_out_of_stock = False

    for sku, qty in cart.items():
        prod = catalog_map.get(sku)
        if prod:
            item_total = prod.price * qty
            subtotal += item_total
            is_oos = not prod.in_stock or prod.stock_qty < qty
            if is_oos:
                has_out_of_stock = True
            cart_items.append({
                "product": prod,
                "quantity": qty,
                "total": item_total,
                "is_out_of_stock": is_oos,
            })

    return render_template(
        "cart.html",
        cart_items=cart_items,
        subtotal=round(subtotal, 2),
        has_out_of_stock=has_out_of_stock,
    )


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    """Add item to shopping cart with quantity validation."""
    sku = request.form.get("sku", "").strip()
    try:
        qty = int(request.form.get("quantity", 1))
        if qty <= 0:
            qty = 1
    except ValueError:
        qty = 1

    product = get_product(sku)
    if not product:
        flash("Invalid product requested.", "danger")
        return redirect(url_for("index"))

    cart = session.get("cart", {})
    cart[sku] = cart.get(sku, 0) + qty
    session["cart"] = cart
    session.modified = True

    if not product.in_stock:
        flash(
            f"'{product.name}' was added to cart, but it is currently OUT OF STOCK. Intelligent substitution is available!",
            "warning",
        )
    else:
        flash(f"Added {qty} × '{product.name}' to cart.", "success")

    return redirect(request.referrer or url_for("index"))


@app.route("/cart/update", methods=["POST"])
def update_cart():
    """Update item quantity or remove item from cart."""
    sku = request.form.get("sku", "").strip()
    action = request.form.get("action", "update")

    cart = session.get("cart", {})
    if sku in cart:
        if action == "remove":
            del cart[sku]
            flash("Item removed from cart.", "info")
        else:
            try:
                new_qty = int(request.form.get("quantity", 1))
                if new_qty > 0:
                    cart[sku] = new_qty
                else:
                    del cart[sku]
            except ValueError:
                pass
        session["cart"] = cart
        session.modified = True

    return redirect(url_for("view_cart"))


# ==========================================
# SUBSTITUTION LOGIC PROTOTYPE WORKFLOW
# ==========================================

@app.route("/substitutions")
def review_substitutions():
    """Intelligent substitution review page for all out-of-stock items in cart."""
    cart = session.get("cart", {})
    catalog = load_catalog_from_db()
    catalog_map = {p.sku: p for p in catalog}

    user_allergens = tuple(session.get("avoid_allergens", []))
    user_tags = tuple(session.get("preferred_tags", []))

    substitution_proposals = []
    for sku, qty in cart.items():
        original = catalog_map.get(sku)
        if original and (not original.in_stock or original.stock_qty < qty):
            suggestion = suggest_substitution(
                original,
                catalog,
                avoid_allergens=user_allergens,
                preferred_tags=user_tags,
                max_price_percent=0.25,
            )
            alternatives = get_all_substitute_candidates(
                original,
                catalog,
                avoid_allergens=user_allergens,
                preferred_tags=user_tags,
            )
            substitution_proposals.append({
                "original": original,
                "quantity": qty,
                "suggestion": suggestion,
                "alternatives": alternatives,
            })

    return render_template(
        "substitutions.html",
        proposals=substitution_proposals,
        avoid_allergens=", ".join(user_allergens),
    )


@app.route("/substitutions/action", methods=["POST"])
def handle_substitution_action():
    """Accept or reject substitution for an out-of-stock item."""
    original_sku = request.form.get("original_sku")
    substitute_sku = request.form.get("substitute_sku")
    action = request.form.get("action")  # 'accept' or 'reject'

    cart = session.get("cart", {})
    sub_log = session.get("substitution_log", {})

    if action == "accept" and original_sku in cart and substitute_sku:
        qty = cart.pop(original_sku)
        cart[substitute_sku] = cart.get(substitute_sku, 0) + qty
        orig_prod = get_product(original_sku)
        sub_prod = get_product(substitute_sku)
        sub_log[substitute_sku] = {
            "original_sku": original_sku,
            "original_name": orig_prod.name if orig_prod else original_sku,
            "fulfilled_name": sub_prod.name if sub_prod else substitute_sku,
            "accepted": True,
            "reason": f"Accepted substitute '{sub_prod.name}' for out-of-stock '{orig_prod.name}'",
        }
        flash(f"Substitution accepted! Replaced '{orig_prod.name}' with '{sub_prod.name}'.", "success")

    elif action == "reject" and original_sku in cart:
        # User rejects substitution; remove the unavailable item or mark as rejected
        qty = cart.pop(original_sku)
        orig_prod = get_product(original_sku)
        sub_log[original_sku] = {
            "original_sku": original_sku,
            "original_name": orig_prod.name if orig_prod else original_sku,
            "accepted": False,
            "reason": "Customer rejected suggested substitution; item removed from order.",
        }
        flash(f"Substitution rejected for '{orig_prod.name}'. Item removed from cart.", "info")

    session["cart"] = cart
    session["substitution_log"] = sub_log
    session.modified = True

    return redirect(url_for("view_cart"))


# ==========================================
# CHECKOUT & ORDER CONFIRMATION
# ==========================================

@app.route("/checkout", methods=["GET"])
def checkout():
    """Checkout page with delivery slot selection and customer details."""
    cart = session.get("cart", {})
    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("index"))

    catalog = load_catalog_from_db()
    catalog_map = {p.sku: p for p in catalog}

    # Verify if any item remains out of stock
    for sku, qty in cart.items():
        prod = catalog_map.get(sku)
        if prod and (not prod.in_stock or prod.stock_qty < qty):
            flash(
                f"'{prod.name}' is out of stock. Please review substitution before proceeding to checkout.",
                "warning",
            )
            return redirect(url_for("review_substitutions"))

    slots = get_delivery_slots()
    subtotal = sum(catalog_map[sku].price * qty for sku, qty in cart.items() if sku in catalog_map)
    delivery_fee = 30.0 if subtotal < 500 else 0.0
    grand_total = subtotal + delivery_fee

    return render_template(
        "checkout.html",
        slots=slots,
        subtotal=round(subtotal, 2),
        delivery_fee=delivery_fee,
        grand_total=round(grand_total, 2),
    )


@app.route("/order/place", methods=["POST"])
def place_order():
    """Validate customer input, check slot capacity, record order in SQLite."""
    cart = session.get("cart", {})
    if not cart:
        flash("Cart is empty.", "danger")
        return redirect(url_for("index"))

    customer_name = request.form.get("customer_name", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()
    slot_id_raw = request.form.get("slot_id")
    dietary_preference = request.form.get("dietary_preference", "").strip()

    # Input validation
    if not customer_name or len(customer_name) < 2:
        flash("Please enter a valid customer name.", "danger")
        return redirect(url_for("checkout"))
    if not phone or len(phone) < 10 or not phone.isdigit():
        flash("Please enter a valid 10-digit contact phone number.", "danger")
        return redirect(url_for("checkout"))
    if not address or len(address) < 8:
        flash("Please enter a complete delivery address.", "danger")
        return redirect(url_for("checkout"))
    if not slot_id_raw:
        flash("Please select an available delivery slot.", "danger")
        return redirect(url_for("checkout"))

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check slot capacity
    cursor.execute("SELECT id, slot_name, capacity, booked FROM delivery_slots WHERE id = ?", (int(slot_id_raw),))
    slot = cursor.fetchone()
    if not slot or (slot["capacity"] - slot["booked"]) <= 0:
        conn.close()
        flash("The selected delivery slot is currently full. Please choose an alternate slot.", "danger")
        return redirect(url_for("checkout"))

    catalog = load_catalog_from_db()
    catalog_map = {p.sku: p for p in catalog}

    # Calculate final total
    subtotal = sum(catalog_map[sku].price * qty for sku, qty in cart.items() if sku in catalog_map)
    delivery_fee = 30.0 if subtotal < 500 else 0.0
    grand_total = subtotal + delivery_fee

    order_code = f"FC-{datetime.datetime.now().strftime('%Y%m%d')}-{secrets.randbelow(8999)+1000}"

    # Insert order
    cursor.execute("""
    INSERT INTO orders (order_code, customer_name, phone, address, slot_name, dietary_preference, total_amount, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, 'Confirmed');
    """, (order_code, customer_name, phone, address, slot["slot_name"], dietary_preference, grand_total))
    order_id = cursor.lastrowid

    # Update booked count on slot
    cursor.execute("UPDATE delivery_slots SET booked = booked + 1 WHERE id = ?", (slot["id"],))

    # Insert order items & update inventory
    sub_log = session.get("substitution_log", {})
    for sku, qty in cart.items():
        prod = catalog_map.get(sku)
        if not prod:
            continue
        sub_info = sub_log.get(sku)
        was_subbed = 1 if sub_info and sub_info.get("accepted") else 0
        orig_sku = sub_info.get("original_sku", sku) if was_subbed else sku
        reason = sub_info.get("reason", "") if was_subbed else ""

        cursor.execute("""
        INSERT INTO order_items (order_id, original_sku, fulfilled_sku, item_name, quantity, unit_price, was_substituted, substitution_reason)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (order_id, orig_sku, sku, prod.name, qty, prod.price, was_subbed, reason))

        # Decrement stock
        cursor.execute("UPDATE products SET stock_qty = MAX(0, stock_qty - ?) WHERE sku = ?", (qty, sku))

    conn.commit()
    conn.close()

    # Clear session cart and substitution tracking
    session["cart"] = {}
    session["substitution_log"] = {}
    session.modified = True

    flash(f"Order #{order_code} successfully placed!", "success")
    return redirect(url_for("order_confirmation", order_code=order_code))


@app.route("/order/confirmation/<order_code>")
def order_confirmation(order_code):
    """Display final order confirmation with items, substitution notes, and delivery slot."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE order_code = ?", (order_code,))
    order = cursor.fetchone()
    if not order:
        conn.close()
        flash("Order not found.", "warning")
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (order["id"],))
    items = cursor.fetchall()
    conn.close()

    return render_template(
        "confirmation.html",
        order=order,
        items=items,
    )


# ==========================================
# MONITORING & HEALTH CHECK ENDPOINTS
# ==========================================

@app.route("/health")
def health_check():
    """Health-check endpoint for continuous monitoring (L4.5)."""
    start_time = datetime.datetime.now()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM products")
        product_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM orders")
        order_count = cursor.fetchone()[0]
        conn.close()
        db_status = "UP"
    except Exception as exc:
        db_status = f"DOWN: {exc}"
        product_count = 0
        order_count = 0

    return jsonify({
        "status": "healthy" if db_status == "UP" else "degraded",
        "service": "FreshCart Online Grocery",
        "case_number": 37,
        "database": db_status,
        "catalog_items": product_count,
        "orders_recorded": order_count,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "version": "1.0.0",
        "prototype_module": "Substitution Logic",
    }), 200 if db_status == "UP" else 500


@app.route("/api/catalog")
def api_catalog():
    """JSON API to fetch full catalog."""
    catalog = load_catalog_from_db()
    return jsonify([
        {
            "sku": p.sku,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "in_stock": p.in_stock,
            "stock_qty": p.stock_qty,
            "allergens": p.allergens,
            "tags": p.tags,
            "unit": p.unit,
        }
        for p in catalog
    ])


@app.route("/api/substitute", methods=["POST"])
def api_substitute():
    """API endpoint for intelligent substitution suggestions."""
    data = request.get_json(silent=True) or {}
    sku = data.get("sku")
    avoid_allergens = tuple(data.get("avoid_allergens", []))
    preferred_tags = tuple(data.get("preferred_tags", []))
    max_price_increase = float(data.get("max_price_increase", 0.0))

    product = get_product(sku)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    catalog = load_catalog_from_db()
    suggestion = suggest_substitution(
        product,
        catalog,
        avoid_allergens=avoid_allergens,
        max_price_increase=max_price_increase,
        preferred_tags=preferred_tags,
    )

    return jsonify({
        "requested_sku": suggestion.requested_sku,
        "selected_sku": suggestion.selected_sku,
        "reason": suggestion.reason,
        "price_difference": suggestion.price_difference,
        "match_score": suggestion.match_score,
        "selected_product_name": suggestion.selected_product.name if suggestion.selected_product else None,
    })


@app.route("/demo/<view_name>")
def demo_view_setup(view_name):
    """Setup session state for browser inspection, testing, and screenshots."""
    if view_name == "cart":
        session["cart"] = {"MIL-002": 1, "MIL-001": 2}
        return redirect(url_for("view_cart"))
    elif view_name == "substitutions":
        session["cart"] = {"MIL-002": 1, "BUT-001": 1}
        return redirect(url_for("review_substitutions"))
    elif view_name == "checkout":
        session["cart"] = {"MIL-001": 2}
        return redirect(url_for("checkout"))
    elif view_name == "confirmation":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT order_code FROM orders ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        code = row["order_code"] if row else "FC-20261124-3701"
        return redirect(url_for("order_confirmation", order_code=code))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

