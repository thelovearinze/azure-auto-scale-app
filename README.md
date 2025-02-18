# Azure Auto-Scaling Flask App

This project is a simple Flask application deployed to Azure App Services with auto-scaling enabled based on CPU utilization. It demonstrates how to configure Azure App Services to automatically scale the number of instances based on demand.

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
    return "Hello from Azure Auto-Scaling Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### 4. Deploy to Azure
- Create a Resource Group: `az group create --name LAResourceGroup --location uksouth`
- Create an App Service Plan: `az appservice plan create --name LAAppServicePlan --resource-group LAResourceGroup --sku S1 --is-linux`
- Create a Web App: `az webapp create --resource-group LAResourceGroup --plan LAAppServicePlan --name my-laflask-app --runtime "PYTHON|3.9"`

### 5. Deploy Flask App
```bash
az webapp up --name my-laflask-app --resource-group LAResourceGroup --runtime "PYTHON|3.9"
```

### 6. Enable Auto-Scaling
- Assign "Monitoring Contributor" Role using Azure CLI.
- Create an auto-scaling setting for the App Service Plan with minimum 1 instance, maximum 3 instances, and a default of 1 instance.
- Add scale-out rule: Increase instance count by 1 when CPU > 70%.
- Add scale-in rule: Decrease instance count by 1 when CPU < 30%.

### 7. Test Auto-Scaling
Simulate load:
```bash
while true; do curl https://my-laflask-app.azurewebsites.net/; done
```
Monitor CPU usage on Azure Portal (App Service Plan -> Metrics -> CPU Percentage).

## GitHub Integration

### 1. Initialize Git
```bash
git init
git add .
git commit -m "Initial commit - Azure auto-scaling Flask app"
```

### 2. Create GitHub Repository
Create a repository on GitHub and obtain the repository URL.

### 3. Push to GitHub
```bash
git remote add origin https://github.com/your-username/azure-auto-scale-app.git
git branch -M main
git push -u origin main
```

**Note:** Use a Personal Access Token (PAT) instead of a password if prompted.

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
