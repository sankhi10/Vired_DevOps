from flask import Flask, request, jsonify

# Creating a server
app = Flask(__name__)

# Sample data: list of students with feedback
students = [
    {"name": "Rahul", "feedback": 4},
    {"name": "Rohit", "feedback": 3},
    {"name": "Rohan", "feedback": 2},
    {"name": "Reshma", "feedback": 2}
]

# Default route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route to get student feedback based on name
@app.route('/student/<name>', methods=['GET'])
def get_students(name):
    student = next((s for s in students if s["name"].lower() == name.lower()), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

# Route to add two numbers
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b
        return jsonify({"a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two integers as query parameters."}), 400

# Route to subtract two numbers
@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a - b
        return jsonify({"a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two integers as query parameters."}), 400

# Route to multiply two numbers
@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a * b
        return jsonify({"a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two integers as query parameters."}), 400

# Route to divide two numbers
@app.route('/divide', methods=['GET'])
def divide_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        result = a / b
        return jsonify({"a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two integers as query parameters."}), 400

if __name__ == '__main__':
    app.run(debug=True)
