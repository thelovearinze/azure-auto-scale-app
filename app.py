from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Auto-Scaling Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Redeploy test
# Redeployment Trigger
# Fresh Deployment Trigger
# Deployment Reset
