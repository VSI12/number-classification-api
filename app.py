from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is Armstrong
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Validate input
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    
    properties.append("odd" if number % 2 else "even")
    
    # Get fun fact from Numbers API
    fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": fun_fact
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the assigned port from Render
    app.run(host="0.0.0.0", port=port)
