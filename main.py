# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialiser l'application FastAPI
app = FastAPI(
    title="Product Catalog API",
    description="Une API simple pour gérer un catalogue de produits"
)

# Définir le modèle Pydantic pour Product
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

# Base de données mock en mémoire
products_db = [
    Product(id=1, name="Laptop", price=999.99, description="High-end gaming laptop"),
    Product(id=2, name="Wireless Mouse", price=29.99, description="Ergonomic wireless mouse"),
    Product(id=3, name="Keyboard", price=59.99),
]

@app.get("/products", response_model=List[Product])
async def list_products():
    """Récupérer la liste de tous les produits du catalogue."""
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Récupérer un produit spécifique par son ID."""
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")