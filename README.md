# Azure Auto-Scaling Flask App

This project is a simple Flask application deployed to Azure App Services with auto-scaling enabled. It demonstrates how to configure Azure App Services to automatically scale the number of instances based on CPU utilization.

## Features
- Flask web application with a simple message response.
- Deployed to Azure App Services.
- Configured auto-scaling based on CPU utilization.

## Prerequisites
- Azure account with an active subscription.
- Azure CLI installed and logged in.
- Python 3.x and virtual environment setup.
- GitHub account for version control.

## Setup and Deployment Steps

### 1. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Required Packages
```bash
pip install flask
pip freeze > requirements.txt
```

### 3. Create `app.py`
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Azure Auto-Scaling Flask App!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### 4. Deploy to Azure App Services
- Create an Azure App Service Plan and a Web App.
- Deploy the Flask app to the Azure Web App using GitHub Actions or Azure CLI.

### 5. Configure Auto-Scaling
- Navigate to the App Service Plan in the Azure Portal.
- Select **Scale out (App Service plan)**.
- Choose **Custom autoscale** and add scale-out and scale-in rules based on CPU utilization (e.g., scale out when CPU > 70%, scale in when CPU < 30%).
- Set **Minimum instance count: 1**, **Maximum instance count: 3**, and **Default instance count: 1**.

**Example Autoscale Settings:**  
![Autoscale Setting](./Screenshot%202025-02-18%20at%2015.26.44.png)

### 6. Simulate High Traffic
Open your terminal and run the following command to simulate continuous requests:
```bash
while true; do curl https://my-laflask-app.azurewebsites.net/; done
```
**Example Traffic Simulation:**  
![Traffic Simulation](./Screenshot%202025-02-18%20at%2015.27.55.png)

### 7. Monitor Metrics
- In the Azure Portal, go to **App Service Plan > Metrics**.
- Track **CPU Percentage** to observe scaling behavior.

**Example CPU Spike:**  
![CPU Metrics](./Screenshot%202025-02-18%20at%2015.33.58.png)

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

