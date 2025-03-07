# Distributed Systems @ University of Tartu

This repository contains the initial code for the practice sessions of the Distributed Systems course at the University of Tartu.

## Getting started

### Overview

The code consists of multiple services. Each service is located in a separate folder. The `frontend` service folder contains a Dockerfile and the code for an example bookstore application. Each backend service folder (e.g. `orchestrator` or `fraud_detection`) contains a Dockerfile, a requirements.txt file and the source code of the service. During the practice sessions, you will implement the missing functionality in these backend services, or extend the backend with new services.

There is also a `utils` folder that contains some helper code or specifications that are used by multiple services. Check the `utils` folder for more information.

### Running the code with Docker Compose [recommended]

To run the code, you need to clone this repository, make sure you have Docker and Docker Compose installed, and run the following command in the root folder of the repository:

```bash
docker compose up
```

This will start the system with the multiple services. Each service will be restarted automatically when you make changes to the code, so you don't have to restart the system manually while developing. If you want to know how the services are started and configured, check the `docker-compose.yaml` file.

The checkpoint evaluations will be done using the code that is started with Docker Compose, so make sure that your code works with Docker Compose.

If, for some reason, changes to the code are not reflected, try to force rebuilding the Docker images with the following command:

```bash
docker compose up --build
```

### Run the code locally

Even though you can run the code locally, it is recommended to use Docker and Docker Compose to run the code. This way you don't have to install any dependencies locally and you can easily run the code on any platform.

If you want to run the code locally, you need to install the following dependencies:

backend services:
- Python 3.8 or newer
- pip
- [grpcio-tools](https://grpc.io/docs/languages/python/quickstart/)
- requirements.txt dependencies from each service

frontend service:
- It's a simple static HTML page, you can open `frontend/src/index.html` in your browser.

And then run each service individually.


Distributed Systems Checkpoint 1

1. User Checkout Submission
1.	The User fills out the checkout form in index.html and clicks “Submit.”
2.	The browser sends a POST request (JSON payload) to the Orchestrator’s /checkout endpoint (Flask).
 
2. Orchestrator Receives Request
1.	The Orchestrator (in orchestrator.py) parses the incoming JSON, generating a unique order_id.
2.	It sets up concurrent or sequential tasks (depending on your configuration) to call each microservice.
 
3. Transaction Verification (gRPC on Port 50052)
1.	The Orchestrator calls VerifyTransaction on the Transaction Verification Service.
2.	The Transaction Verification Service checks:
o	Required fields (e.g., user name, credit card number).
o	Credit card format (16 digits).
o	Expiration date (MM/YY) to ensure it’s not expired.
o	CVV format (3–4 digits).
3.	It returns a TransactionVerificationResponse with verification=True or False, plus any error messages.
o	If verification fails, the Orchestrator rejects the order and responds to the user.
o	If verification passes, the Orchestrator proceeds to Fraud Detection.
 
4. Fraud Detection (gRPC on Port 50051)
1.	Having confirmed the card is valid, the Orchestrator next calls DetectUserFraud on the Fraud Detection Service.
2.	The Fraud Detection Service:
o	Loads its local XGBoost model (fraud_detection.pkl).
o	Extracts features (e.g., total_num_items, billing_shipping_match, name_match).
o	Predicts whether the order is fraudulent or safe.
3.	It returns a FraudDetectionResponse with a boolean isFraudulent and a reason if fraud is detected.
o	If fraud is detected, the Orchestrator sends “Order Rejected” (with the reason) to the user.
o	If not fraudulent, the Orchestrator proceeds to get Suggestions.
 
5. Suggestions Service (gRPC on Port 50053)
1.	The Orchestrator calls SuggestBooks on the Suggestions Service, providing (for example) the first book’s title from the order.
2.	The Suggestions Service:
o	Uses the google.genai client to send a prompt to the Gemini API over HTTPS.
o	Parses the returned JSON list of recommended books.
o	Returns a SuggestionsResponse to the Orchestrator.
 
6. Aggregating Results & Final Response
1.	The Orchestrator compiles the verification (Transaction Verification), fraud check (Fraud Detection), and recommendations (Suggestions).
2.	If either Transaction Verification fails or Fraud Detection deems the order fraudulent, the Orchestrator returns:
json
Copy
{
  "orderId": "<uuid>",
  "status": "Order Rejected",
  "suggestedBooks": []
}
3.	Otherwise, the Orchestrator returns:
json
Copy
{
  "orderId": "<uuid>",
  "status": "Order Approved",
  "suggestedBooks": [ ... ]
}
4.	The User sees this final JSON response in the browser, indicating success or rejection and any recommended books


