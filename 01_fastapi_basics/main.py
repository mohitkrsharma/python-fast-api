from fastapi import FastAPI
from pydantic import BaseModel
# create app instance
app = FastAPI()

# Home Route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI, Mohit!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}

# GET with query params: /items/?name=keyboard&price=500
@app.get("/items/")
def read_items(name: str, price:float =0.0):
    return {"item_name": name, "item_price": price}

# Handling POST Request with JSON Body
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_offer: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"messgae":"Item created successfully!", "item": item}

# PUT Request – Update an Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item with id {item_id} updated successfully!", "item": item}

#  DELETE Request – Remove an Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with id {item_id} deleted successfully!"}


# Mini Assignment
# 1. Return a hardcoded list of products.
# 2. Return details of a product by ID. If product is not found, return a custom 404 message.
# 3. Accept a product in the request body using Pydantic model and return it back with a success message.
# 4. Update the product details. Just return back what was updated.
# 5. Delete the product and return a message like: Product with id 3 deleted successfully

# Hardcoded list of products
product_list = [
    {"id": 1, "name": "Laptop", "price": 1000.0},
    {"id": 2, "name": "Smartphone", "price": 500.0},
    {"id": 3, "name": "Tablet", "price": 300.0}
]

# Create indexes for faster search by name and price
product_name_index = {product["name"].lower(): product for product in product_list}
product_price_index = {product["price"]: product for product in product_list}

# Define a Pydantic model for Product
class Product(BaseModel):
    id: int
    name: str
    price: float

# Endpoint to get all products
@app.get("/products/")
def get_all_products():
    """
    Returns a list of all products.
    """
    return {"products": product_list}

# Endpoint to get a product by its ID
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    """
    Returns the details of a product by its ID.
    If the product is not found, raises a 404 HTTP exception.
    """
    for product in product_list:
        if product["id"] == product_id:
            return {"product": product}
    from fastapi import HTTPException  # Add this import at the top of the file if not already present
    raise HTTPException(status_code=404, detail="Product not found!")

# Endpoint to search for products by name or price
from typing import Optional  # Add this import at the top of the file if not already present

@app.get("/products/search/")
def search_product(name: Optional[str] = None, price: Optional[float] = None):
    """
    Searches for products by name or price.
    Returns a list of matching products or a message if no products are found.
    """
    results = []
    if name:
        product = product_name_index.get(name.lower())
        if product:
            results.append(product)
    if price:
        product = product_price_index.get(price)
        if product and product not in results:
            results.append(product)
    return {"products": results} if results else {"message": "No products found!"}

# Endpoint to create a new product
@app.post("/products/")
def create_product(product: Product):
    """
    Accepts a product in the request body and adds it to the product list.
    Returns a success message along with the created product.
    """
    product_list.append(product.dict())
    return {"message": "Product created successfully!", "product": product}

# Endpoint to update an existing product by its ID
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    """
    Updates the details of an existing product by its ID.
    Returns a success message along with the updated product.
    If the product is not found, returns a not found message.
    """
    for idx, p in enumerate(product_list):
        if p["id"] == product_id:
            product_list[idx] = product.dict()
            return {"message": "Product updated successfully!", "product": product}
    return {"message": "Product not found!"}

# Endpoint to delete a product by its ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """
    Deletes a product by its ID.
    Returns a success message if the product is deleted.
    If the product is not found, returns a not found message.
    """
    for idx, product in enumerate(product_list):
        if product["id"] == product_id:
            del product_list[idx]
            return {"message": f"Product with id {product_id} deleted successfully!"}
    return {"message": "Product not found!"}