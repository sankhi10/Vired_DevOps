from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
products = [
    {"id": 100, "name": "Mobile", "Desc": "cell phones"},
    {"id": 101, "name": "Television", "Desc": "smart tv"},
]

# Route to get all products using GET method only
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a specific product by ID using GET method only
@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = next((product for product in products if product["id"] == id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
