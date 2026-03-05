from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB-C Cable", "price": 299, "category": "Accessories", "in_stock": True},
    {"id": 3, "name": "Bluetooth Speaker", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 999, "category": "Accessories", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 3499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1999, "category": "Electronics", "in_stock": True}
]
#Q1
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

#Q2
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {"products": filtered_products}

#Q3
@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }

#Q4
@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }

#Q5
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }

#Bonus
@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }
