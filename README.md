# Insurance Premium Prediction API

A machine learning-powered REST API that predicts insurance premiums based on customer demographics and lifestyle factors. Built with FastAPI for high performance and automatic API documentation.

## 🚀 Features

- 🤖 **ML-Powered Predictions**: Accurate premium estimation using trained models
- ⚡ **FastAPI Framework**: High-performance async API with automatic documentation
- 📊 **Multiple Factors**: Consider BMI, age, lifestyle, income, and occupation
- 🔍 **Input Validation**: Pydantic schemas for robust data validation
- 📖 **Auto Documentation**: Interactive API docs with Swagger UI
- 🏥 **Health Monitoring**: Built-in health check endpoints
- 🐳 **Docker Ready**: Easy containerization and deployment

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Usage](#installation--usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Schema Validation](#schema-validation)
- [Development](#development)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)

## 📁 Project Structure

```
Insurance-Premium-Prediction/
├── app.py                      # Main FastAPI application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration (if present)
├── schema/                     # Pydantic data models
│   ├── user_input.py          # Input validation schema
│   └── prediction_response.py # Response schema
├── Model/                      # Machine learning components
│   └── predict.py             # Prediction logic and model loading
├── config/                     # Configuration files
│   └── ...                    # Configuration settings
└── README.md                   # Project documentation
```

## 🔧 Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, for containerization)

## 🚀 Installation & Usage

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Insurance-Premium-Prediction.git
   cd Insurance-Premium-Prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API server**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API**
   - **API Base URL**: `http://localhost:8000`
   - **Interactive Docs**: `http://localhost:8000/docs`
   - **Alternative Docs**: `http://localhost:8000/redoc`

## 🌐 API Endpoints

### Base Endpoints

#### `GET /`
Welcome message and API information
```json
{
  "message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."
}
```

#### `GET /health`
Health check endpoint for monitoring
```json
{
  "status": "OK",
  "version": "1.0.0",
  "model_loaded": true
}
```

### Prediction Endpoint

#### `POST /predict`
Predict insurance premium based on user input

**Request Body:**
```json
{
  "bmi": 25.5,
  "age_group": "30-40",
  "lifestyle_risk": "medium",
  "city_tier": "tier1",
  "income_lpa": 8.5,
  "occupation": "engineer"
}
```

**Response:**
```json
{
  "predicted_premium": 15750.25
}
```

**Error Response:**
```json
{
  "error": "Model prediction failed: Invalid input format"
}
```

## 📊 Input Parameters

| Parameter | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `bmi` | float | Body Mass Index | 18.5 - 40.0 |
| `age_group` | string | Age category | "20-30", "30-40", "40-50" |
| `lifestyle_risk` | string | Risk assessment | "low", "medium", "high" |
| `city_tier` | string | City classification | "tier1", "tier2", "tier3" |
| `income_lpa` | float | Annual income (lakhs) | 2.5 - 50.0 |
| `occupation` | string | Job category | "engineer", "doctor", "teacher" |

## 🤖 Model Information

The prediction model considers multiple factors:

- **Health Metrics**: BMI as a health indicator
- **Demographics**: Age group classification
- **Risk Assessment**: Lifestyle-based risk factors
- **Geographic**: City tier for regional variations
- **Economic**: Income level considerations
- **Professional**: Occupation-based risk profiling

### Model Pipeline
- Data preprocessing and validation
- Feature engineering and encoding
- ML model prediction
- Post-processing and formatting

## 🔍 Schema Validation

The API uses Pydantic schemas for robust input/output validation:

### UserInput Schema (`schema/user_input.py`)
- Type validation for all input fields
- Range validation for numerical values
- Enum validation for categorical fields
- Custom validation rules

### PredictionResponse Schema (`schema/prediction_response.py`)
- Structured response format
- Type safety for API responses
- Error handling schemas

## 🛠️ Development

### Running with Development Server
```bash
# With auto-reload for development
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing the API

#### Using curl
```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Make prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "bmi": 25.5,
    "age_group": "30-40",
    "lifestyle_risk": "medium",
    "city_tier": "tier1",
    "income_lpa": 8.5,
    "occupation": "engineer"
  }'
```

#### Using Python requests
```python
import requests

# API endpoint
url = "http://localhost:8000/predict"

# Sample data
data = {
    "bmi": 25.5,
    "age_group": "30-40",
    "lifestyle_risk": "medium",
    "city_tier": "tier1",
    "income_lpa": 8.5,
    "occupation": "engineer"
}

# Make request
response = requests.post(url, json=data)
print(response.json())
```

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Commands
```bash
# Build image
docker build -t insurance-premium-api .

# Run container
docker run -p 8000:8000 insurance-premium-api

# Run in background
docker run -d -p 8000:8000 insurance-premium-api
```

## ☁️ Cloud Deployment

### Railway/Render/Heroku
Update your startup command:
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

### AWS/GCP/Azure
The API is ready for deployment on major cloud platforms with container services.

## 📈 Performance Optimization

- **Async Support**: FastAPI's async capabilities for concurrent requests
- **Model Caching**: Efficient model loading and caching
- **Input Validation**: Fast Pydantic validation
- **Error Handling**: Robust exception management

## 🔧 Configuration

The `config/` folder contains:
- Model configuration settings
- API configuration parameters
- Environment-specific settings
- Feature engineering parameters

## 🛠️ Troubleshooting

### Common Issues

1. **Model loading errors**
   ```bash
   # Check if model files exist in Model/ directory
   # Verify model compatibility
   ```

2. **Port already in use**
   ```bash
   # Use different port
   uvicorn app:app --port 8001
   ```

3. **Dependency conflicts**
   ```bash
   # Create fresh virtual environment
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 📋 Key Dependencies

- **FastAPI**: Modern web framework for APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn**: Machine learning library
- **pandas/numpy**: Data manipulation and computation
- **Streamlit**: For optional web interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest`
6. Commit changes: `git commit -am 'Add feature'`
7. Push to branch: `git push origin feature-name`
8. Submit a pull request

## 📊 API Usage Examples

### Batch Predictions
```python
import requests
import json

# Multiple predictions
customers = [
    {"bmi": 22.5, "age_group": "25-35", "lifestyle_risk": "low", 
     "city_tier": "tier1", "income_lpa": 12.0, "occupation": "doctor"},
    {"bmi": 28.0, "age_group": "35-45", "lifestyle_risk": "high", 
     "city_tier": "tier2", "income_lpa": 6.5, "occupation": "teacher"}
]

for customer in customers:
    response = requests.post("http://localhost:8000/predict", json=customer)
    print(f"Premium: ₹{response.json()['predicted_premium']}")
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI documentation and community
- scikit-learn for machine learning capabilities
- Insurance industry data providers
- Open-source Python ecosystem

## 📞 Support

If you encounter any issues:
1. Check the [Issues](https://github.com/mbe-waqar/Insurance-Premium-Prediction/issues) page
2. Review the API documentation at `/docs`
3. Create a new issue with detailed information
4. Include API request/response examples

---

**⭐ If you find this project helpful, please give it a star!**

**Made with ❤️ by [Waqar Ali](https://www.linkedin.com/in/waqar-ali-b70976322/) using FastAPI and Machine Learning**