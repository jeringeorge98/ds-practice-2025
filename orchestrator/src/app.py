import sys
import os
import uuid
import concurrent.futures
import time
# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if "__file__" in globals() else os.getenv("PYTHONFILE", "")
fraud_detection_grpc_path = os.path.abspath(
    os.path.join(FILE, "../../../utils/pb/bookstore/fraud_detection")
)
suggestions_path = os.path.abspath(os.path.join(FILE, "../../../utils/pb/bookstore/suggestions"))
transaction_verficiation_path = os.path.abspath(os.path.join(FILE, "../../../utils/pb/bookstore/transaction_verification"))
sys.path.insert(0, fraud_detection_grpc_path)
sys.path.insert(1, suggestions_path)
import fraud_detection_pb2_grpc as fraud_detection_grpc
import fraud_detection_pb2 as fraud_detection
# import fraud_detection_pb2_grpc as fraud_detection_grpc
# import transaction_verification_pb2 as transaction_verification
# import transaction_verification_pb2_grpc as transaction_verification_grpc
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc
import grpc

from datetime import datetime


# def greet(name="you"):
#     # Establish a connection with the fraud-detection gRPC service.
#     with grpc.insecure_channel("fraud_detection:50051") as channel:
#         # Create a stub object.
#         stub = fraud_detection_grpc.HelloServiceStub(channel)
#         # Call the service through the stub object.
#         response = stub.SayHello(fraud_detection.HelloRequest(name=name))
#     return response.greeting

 
# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request,jsonify
from flask_cors import CORS
import json

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app, resources={r"/*": {"origins": "*"}})


def connect_to_transaction_verification_service(order_info):
    # with grpc.insecure_channel('transaction_verification:50052') as channel:
    #     stub = transaction_verification_grpc.TransactionVerificationServiceStub(channel)
    #     response = stub.VerifyTransaction(order_info)
    #     print("Transaction Verification Response:", response)
        time.sleep(5)
        return {"dummyresponse":"dummyresponse"}
def connect_to_fraud_detection_service(order_info):
    # with grpc.insecure_channel('fraud_detection:50051') as channel:
    #     stub = fraud_detection_grpc.FraudDetectionServiceStub(channel)
    #     user_fraud_response = stub.DetectUserFraud(order_info)
    #     credit_card_fraud_response = stub.DetectCreditCardFraud(order_info)        
    #     print("Fraud Detection Response:", user_fraud_response,credit_card_fraud_response)
        time.sleep(8)
        response={"user_fraud_response":"user_fraud_response","credit_card_fraud_response":"credit_card_fraud_response"}
        return response

# def connect_to_suggestions_service(ordered_books):
#     with grpc.insecure_channel('suggestions:50053') as channel:
#         stub = suggestions_grpc.SuggestionsServiceStub(channel)
#         response = stub.getSuggestions(ordered_books)
#         print("Suggestions Response:", response)
#         return response

def detectUserFraud(order_info):
    print("Order Info received in detectUserFraud:", order_info)
    try:
        # Create the request using constructor-style initialization
        request = fraud_detection.OrderInfo(
            user=fraud_detection.User(
                name=order_info.get('user', {}).get('name', ''),
                contact=order_info.get('user', {}).get('contact', ''),
                cardHolderName=order_info.get('user', {}).get('cardHolderName', '')
            ),
            creditCard=fraud_detection.CreditCard(
                number=order_info.get('creditCard', {}).get('number', ''),
                expirationDate=order_info.get('creditCard', {}).get('expirationDate', ''),
                cvv=order_info.get('creditCard', {}).get('cvv', '')
            ),
            items=[
                fraud_detection.OrderItem(
                    name=item.get('name', ''),
                    quantity=item.get('quantity', 0)
                ) for item in order_info.get('items', [])
            ],
            billingAddress=fraud_detection.Address(
                street=order_info.get('billingAddress', {}).get('street', ''),
                city=order_info.get('billingAddress', {}).get('city', ''),
                country=order_info.get('billingAddress', {}).get('country', '')
            ),
            shippingAddress=fraud_detection.Address(
                street=order_info.get('shippingAddress', {}).get('street', ''),
                city=order_info.get('shippingAddress', {}).get('city', ''),
                country=order_info.get('shippingAddress', {}).get('country', '')
            ),
            userComment=order_info.get('userComment', ''),
            shippingMethod=order_info.get('shippingMethod', ''),
            giftWrapping=order_info.get('giftWrapping', False),
            termsAccepted=order_info.get('termsAccepted', False)
        )
        
        print("Final request object:", request)
        
        with grpc.insecure_channel("fraud_detection:50051") as channel:
            stub = fraud_detection_grpc.FraudDetectionServiceStub(channel)
            response = stub.DetectUserFraud(request)
            print("Fraud Detection Response:", response)
            return response
    except Exception as e:
        print(f"Error in detectUserFraud: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise

def suggestBooks(order):
    request = suggestions.BookRequest(
        book_name=order.get("items", [{}])[0].get("name", "")
    )
    with grpc.insecure_channel("suggestions:50053") as channel:
        stub = suggestions_grpc.SuggestionsServiceStub(channel)
        
        response = stub.SuggestBooks(request)
        print("Suggestions Response:", response)
    return {"suggestedBooks": [{"title": response.suggestions}]}


# Define a GET endpoint.
@app.route("/", methods=["GET"])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    #response = greet(name="Jerin")
    # Return the response.
    return "Server UP"
def parse_suggested_books(suggested_books_json):
    suggested_books_list = []
    for book in suggested_books_json:
        # Assuming 'title' is a list of book details
        for book_detail in book['title']:
            book_id = str(uuid.uuid4())
            suggested_books_list.append({
                "bookId": book_id,
                "title": book_detail.book_title,
                "author": book_detail.book_author
            })
    # print(suggested_books_list, "suggested_books_list in right format")
    return suggested_books_list

@app.route("/checkout", methods=["POST"])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    try:
        order_id = str(uuid.uuid4())
        # Get request object data to json
        request_data = request.get_json() if request.is_json else json.loads(request.data)
        print("Received request data:", request_data)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            fraud_future = executor.submit(detectUserFraud, request_data)
            fraud_response = fraud_future.result()
            print("Fraud Response:", fraud_response.isFraudulent, fraud_response.reason, time.time())
            
            if fraud_response.isFraudulent:
                return jsonify(
                    {
                        "orderId": order_id,
                        "status": "Order Rejected",
                        "suggestedBooks": []
                    }
                )
            
            # order_status_response = {
            #     "orderId": order_id,
            #     "status": "Order Approved"
            # }
            order_status_response = {
                "orderId": order_id,
                "status": "Order Approved",
                "suggestedBooks": [
                    {"bookId": "123", "title": "The Best Book", "author": "Author 1"},
                    {"bookId": "456", "title": "The Second Best Book", "author": "Author 2"},
                ],
            }
            
        return order_status_response
    except Exception as e:
        print(f"Error in checkout: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return {
            "orderId": str(order_id),
            "status": "Order Failed",
            "error": str(e)
        }, 500

if __name__ == "__main__":
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host="0.0.0.0")
