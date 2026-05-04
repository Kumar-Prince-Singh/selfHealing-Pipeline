from flask import Flask
import random
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # 20% chance of random failure to test self-healing
    if random.random() < 0.2:
        return "Random failure occurred! Retrying...", 500
    return "Hello from Self-Healing Pipeline! 🚀", 200

@app.route('/health')
def health():
    return "OK", 200

@app.route('/fail')
def force_fail():
    """Endpoint to force failure for testing self-healing"""
    return "Forced failure!", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)