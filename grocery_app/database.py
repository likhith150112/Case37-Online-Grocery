"""SQLite Database Layer for Online Grocery Application.

Case 37: Online Grocery
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)
"""

import os
import sqlite3
from typing import Dict, List, Optional
from grocery_app.substitution import Product

DB_PATH = os.path.join(os.path.dirname(__file__), "grocery.db")


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(seed: bool = True):
    """Initialize database schema and seed initial grocery data."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        sku TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        in_stock INTEGER NOT NULL,
        stock_qty INTEGER NOT NULL DEFAULT 10,
        allergens TEXT DEFAULT '',
        tags TEXT DEFAULT '',
        unit TEXT DEFAULT '1 unit',
        description TEXT DEFAULT ''
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS delivery_slots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slot_name TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        capacity INTEGER NOT NULL DEFAULT 10,
        booked INTEGER NOT NULL DEFAULT 0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_code TEXT UNIQUE NOT NULL,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        slot_name TEXT NOT NULL,
        dietary_preference TEXT DEFAULT '',
        total_amount REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'Placed',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        original_sku TEXT NOT NULL,
        fulfilled_sku TEXT NOT NULL,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit_price REAL NOT NULL,
        was_substituted INTEGER NOT NULL DEFAULT 0,
        substitution_reason TEXT DEFAULT '',
        FOREIGN KEY (order_id) REFERENCES orders (id)
    );
    """)

    if seed:
        cursor.execute("SELECT COUNT(*) FROM products")
        if cursor.fetchone()[0] == 0:
            seed_initial_data(cursor)

    conn.commit()
    conn.close()


def seed_initial_data(cursor: sqlite3.Cursor):
    """Seed catalog with realistic grocery products including out-of-stock items."""
    products_data = [
        # Dairy Category
        ("MIL-001", "Nandini Toned Fresh Milk 1L", "Dairy", 44.0, 1, 25, "", "toned,local,fresh", "1 L Pouch", "Pasteurised toned milk with 3.0% fat."),
        ("MIL-002", "Amul Taaza Homogenised Milk 1L", "Dairy", 54.0, 0, 0, "", "toned,long-life", "1 L Tetra", "UHT treated long life toned milk."),
        ("MIL-003", "Mother Dairy Full Cream Milk 1L", "Dairy", 66.0, 1, 15, "", "full-cream,rich", "1 L Pouch", "Standardised full cream milk with 6.0% fat."),
        ("MIL-004", "Epigamia Almond Drink Vanilla 1L", "Dairy", 120.0, 1, 8, "tree-nut", "vegan,dairy-free", "1 L Bottle", "Plant-based milk made from California almonds."),
        ("BUT-001", "Amul Salted Table Butter 500g", "Dairy", 275.0, 0, 0, "", "salted,spread", "500 g Pack", "Classic Indian pasteurised table butter."),
        ("BUT-002", "Nandini Pure Butter Salted 500g", "Dairy", 250.0, 1, 12, "", "salted,local", "500 g Pack", "Karnataka Milk Federation fresh salted table butter."),
        ("PDR-001", "Milky Mist Fresh Paneer 200g", "Dairy", 95.0, 1, 18, "", "fresh,paneer", "200 g Pack", "Soft malai paneer cube for curries."),

        # Staples & Grains Category
        ("RIC-001", "India Gate Basmati Rice Feast 1kg", "Staples", 140.0, 0, 0, "", "basmati,premium", "1 kg Bag", "Aged long grain aromatic basmati rice."),
        ("RIC-002", "Daawat Rozana Basmati Rice 1kg", "Staples", 145.0, 1, 20, "", "basmati,everyday", "1 kg Bag", "Fluffy everyday basmati rice grains."),
        ("RIC-003", "Fortune Everyday Basmati Rice 1kg", "Staples", 130.0, 1, 14, "", "basmati,budget", "1 kg Bag", "Long grain basmati for daily culinary use."),
        ("ATT-001", "Aashirvaad Shudh Chakki Atta 5kg", "Staples", 260.0, 1, 30, "gluten", "whole-wheat,chakki", "5 kg Bag", "100% whole wheat atta with 0% maida."),
        ("ATT-002", "Pillsbury Chakki Fresh Atta 5kg", "Staples", 255.0, 0, 0, "gluten", "whole-wheat,chakki", "5 kg Bag", "Stone-ground whole wheat flour."),
        ("OIL-001", "Fortune Sunlite Refined Sunflower Oil 1L", "Staples", 135.0, 1, 22, "", "refined,cooking-oil", "1 L Pouch", "Light and healthy cooking sunflower oil."),

        # Fruits & Fresh Produce Category
        ("VEG-001", "Fresh Hybrid Tomato 1kg", "Fresh Produce", 35.0, 1, 40, "", "fresh,vegetable,local", "1 kg Net", "Farm-fresh ripe red firm tomatoes."),
        ("VEG-002", "Farm Fresh Jyoti Potato 1kg", "Fresh Produce", 30.0, 1, 50, "", "fresh,vegetable,local", "1 kg Net", "Washed, unblemished clean potatoes."),
        ("VEG-003", "Fresh Red Onion 1kg", "Fresh Produce", 45.0, 1, 35, "", "fresh,vegetable,local", "1 kg Net", "Medium-sized pungent red onions."),
        ("FRU-001", "Shimla Royal Apples 1kg", "Fresh Produce", 180.0, 0, 0, "", "apple,fruit,sweet", "1 kg Box (4 pcs)", "Crisp and juicy Himalayan red apples."),
        ("FRU-002", "Kashmir Kinnaur Delicious Apples 1kg", "Fresh Produce", 170.0, 1, 16, "", "apple,fruit,sweet", "1 kg Box (4 pcs)", "Sweet hand-picked red Kashmiri apples."),
        ("FRU-003", "Robusta Fresh Yellow Banana 1kg", "Fresh Produce", 48.0, 1, 25, "", "banana,fruit,local", "1 kg Bunch", "Naturally ripened sweet bananas."),

        # Bakery & Breakfast Category
        ("BRD-001", "Britannia 100% Whole Wheat Bread 400g", "Bakery", 50.0, 0, 0, "gluten", "whole-wheat,brown", "400 g Loaf", "Healthy brown loaf baked from whole grain."),
        ("BRD-002", "Modern 100% Whole Wheat Bread 400g", "Bakery", 48.0, 1, 12, "gluten", "whole-wheat,brown", "400 g Loaf", "Fiber-rich whole wheat bakery bread."),
        ("BRD-003", "Britannia Vita Rich Milk Bread 400g", "Bakery", 45.0, 1, 15, "gluten", "white,milk", "400 g Loaf", "Soft enriched sweet sandwich bread."),
        ("EGG-001", "Farm Fresh White Eggs (Pack of 6)", "Bakery", 48.0, 1, 30, "egg", "protein,poultry", "6 Pcs Pack", "Graded farm fresh protein white eggs."),
    ]

    cursor.executemany("""
    INSERT INTO products (sku, name, category, price, in_stock, stock_qty, allergens, tags, unit, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, products_data)

    slots_data = [
        ("Morning Slot (07:00 AM – 09:00 AM)", "07:00", "09:00", 10, 4),
        ("Mid-Day Slot (11:00 AM – 01:00 PM)", "11:00", "13:00", 10, 7),
        ("Evening Slot (05:00 PM – 07:00 PM) [FULL]", "17:00", "19:00", 10, 10),
        ("Night Slot (08:00 PM – 10:00 PM)", "20:00", "22:00", 10, 2),
    ]

    cursor.executemany("""
    INSERT INTO delivery_slots (slot_name, start_time, end_time, capacity, booked)
    VALUES (?, ?, ?, ?, ?);
    """, slots_data)


def load_catalog_from_db() -> List[Product]:
    """Load all products from database into Product dataclass objects."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sku, name, category, price, in_stock, stock_qty, allergens, tags, unit, description FROM products")
    rows = cursor.fetchall()
    conn.close()

    catalog = []
    for row in rows:
        allergens = tuple(x.strip() for x in row["allergens"].split(",") if x.strip())
        tags = tuple(x.strip() for x in row["tags"].split(",") if x.strip())
        catalog.append(
            Product(
                sku=row["sku"],
                name=row["name"],
                category=row["category"],
                price=float(row["price"]),
                in_stock=bool(row["in_stock"]),
                stock_qty=int(row["stock_qty"]),
                allergens=allergens,
                tags=tags,
                unit=row["unit"],
                description=row["description"],
            )
        )
    return catalog


def get_product(sku: str) -> Optional[Product]:
    """Retrieve single product by SKU."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sku, name, category, price, in_stock, stock_qty, allergens, tags, unit, description FROM products WHERE sku = ?", (sku,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    allergens = tuple(x.strip() for x in row["allergens"].split(",") if x.strip())
    tags = tuple(x.strip() for x in row["tags"].split(",") if x.strip())
    return Product(
        sku=row["sku"],
        name=row["name"],
        category=row["category"],
        price=float(row["price"]),
        in_stock=bool(row["in_stock"]),
        stock_qty=int(row["stock_qty"]),
        allergens=allergens,
        tags=tags,
        unit=row["unit"],
        description=row["description"],
    )


def get_delivery_slots() -> List[Dict]:
    """Retrieve all delivery slots with their available capacity."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, slot_name, start_time, end_time, capacity, booked FROM delivery_slots ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    slots = []
    for r in rows:
        available = r["capacity"] - r["booked"]
        slots.append({
            "id": r["id"],
            "slot_name": r["slot_name"],
            "start_time": r["start_time"],
            "end_time": r["end_time"],
            "capacity": r["capacity"],
            "booked": r["booked"],
            "available": available,
            "is_full": available <= 0,
        })
    return slots

