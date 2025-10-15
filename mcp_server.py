# mcp_server.py
import sys
from pathlib import Path

# S'assurer que la racine du projet est dans le chemin Python
sys.path.append(str(Path(__file__).parent))

from fastmcp import FastMCP
from main import products_db, Product
from typing import List

# Initialiser FastMCP
mcp = FastMCP(
    name="Product Catalog MCP Server",
)

@mcp.tool()
def list_products() -> List[dict]:
    """Lister tous les produits disponibles avec leur ID, nom, prix et description."""
    return [product.model_dump() for product in products_db]

@mcp.tool()
def get_product(product_id: int) -> dict:
    """Récupérer les détails d'un produit spécifique par son ID.
    
    Args:
        product_id: L'identifiant unique du produit
    """
    for product in products_db:
        if product.id == product_id:
            return product.model_dump()
    return {"error": "Product not found"}

if __name__ == "__main__":
    mcp.run()