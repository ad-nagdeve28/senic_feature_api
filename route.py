from flask import Blueprint, jsonify, request
from fetch_products import SenicProducts

# Initialize Blueprint
api = Blueprint("api", __name__)

# Initialize the product scraper
senic = SenicProducts()

@api.route('/products', methods=['GET'])
def get_all_products():
    """Fetch all available product images."""
    return jsonify({"products": senic.products})

@api.route('/products/search', methods=['GET'])
def search_product():
    """Search for a product by name."""
    product_name = request.args.get('name', '').strip()
    
    if not product_name:
        return jsonify({"error": "Product name parameter is required"}), 400

    result = senic.search_product(product_name)
    
    if result:
        return jsonify({"results": result})
    else:
        return jsonify({"message": f"No products found for '{product_name}'"}), 404
