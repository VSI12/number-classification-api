# Number Classification API

## Overview
The **Number Classification API** allows users to input a number and retrieve its mathematical properties along with a fun fact from the [Numbers API](http://numbersapi.com/). The API determines whether the number is prime, perfect, Armstrong, and whether it is odd or even.

## Features
- Determines if a number is **prime**, **perfect**, or **Armstrong**.
- Identifies whether the number is **odd** or **even**.
- Computes the **sum of its digits**.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns responses in **JSON format**.
- Supports **CORS** for cross-origin requests.
- Deployed to a publicly accessible endpoint.

## API Specification

### **Endpoint:**
`GET /api/classify-number?number=<number>`

### **Example Request:**
```sh
curl -X GET "<your-deployment-url>/api/classify-number?number=371"
```

### **Success Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request):**
```json
{
    "number": "abc",
    "error": true
}
```

## Installation & Local Development

### **Prerequisites:**
- Python 3.x
- `pip` package manager

### **Clone the Repository:**
```sh
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

### **Install Dependencies:**
```sh
pip install -r requirements.txt
```

### **Run the API Locally:**
```sh
python app.py
```

### **Test Locally:**
Visit `http://127.0.0.1:5000/api/classify-number?number=371` in your browser or use Postman/cURL.

## Deployment
This API is deployed to a publicly accessible platform. You can deploy it using services like:
- **Render**: (Recommended for Flask apps)
- **Railway.app**
- **AWS Lambda + API Gateway** (For serverless deployment)
- **Docker + ECS**

### **Deploying to Render (Example):**
1. Push your code to a GitHub repository.
2. Sign up at [Render](https://render.com/).
3. Create a new **Web Service**.
4. Connect your GitHub repository and deploy.

## Technologies Used
- **Flask** (Python web framework)
- **Flask-CORS** (Cross-Origin Resource Sharing)
- **Requests** (For fetching fun facts from Numbers API)
- **GitHub** (Version Control)

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes and push.
4. Create a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For questions or issues, reach out via [GitHub Issues](https://github.com/yourusername/number-classification-api/issues).

