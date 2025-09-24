"""
API Gateway Stub using Flask
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    """
    Returns API status in format expected by tests.
    """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
