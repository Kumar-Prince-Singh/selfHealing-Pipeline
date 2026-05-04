from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # 20% chance of random failure to test self-healing
    if random.random() < 0.2:
        return "Random failure occurred!", 500
    return "Hello from Self-Healing Pipeline!", 200

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)