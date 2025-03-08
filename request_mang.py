from flask import Flask, request, jsonify
from fetch_products import SenicProducts

app = Flask(__name__)
senic = SenicProducts()

@app.route('/')
def get_products():
    products = senic.get_products()
    return products

@app.route('/product')
def find_product():
    product_name = request.args.get("name", "")
    product = get_products()
    if not product_name:
         return jsonify({"error": "Please provide a product name"}), 400
    result = senic.search_product(product_name=product_name)
    return jsonify(result)

if __name__ == "__main__":
    app.run()