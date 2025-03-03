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
sys.path.insert(0, suggestions_path)
import fraud_detection_pb2_grpc as fraud_detection_grpc
import fraud_detection_pb2 as fraud_detection
# import fraud_detection_pb2_grpc as fraud_detection_grpc
# import transaction_verification_pb2 as transaction_verification
# import transaction_verification_pb2_grpc as transaction_verification_grpc
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc
import grpc


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
from flask import Flask, request
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
    order_id=uuid.uuid4()
    # Get request object data to json
    request_data = json.loads(request.data)
    order_status_response ={}
    # Print request object data
    print("Request Data:", request_data)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
     #verification_future =  executor.submit(connect_to_transaction_verification_service,request_data)
     #fraud_future =  executor.submit(connect_to_fraud_detection_service,request_data)
    #  suggestions_future= executor.submit(suggestBooks,request_data)
     
     #verification_response = verification_future.result()
     #fraud_response = fraud_future.result()
    #  suggestions_response = suggestions_future.result()
     
     #print("Verification Response:", verification_response,time.time())
     #print("Fraud Response:", fraud_response,time.time())
    #  print("Suggestions Response:", suggestions_response['suggestedBooks'],time.time())
    #  suggested_books_json = suggestions_response['suggestedBooks'] 
             
     # call 
    # Dummy response following the provided YAML specification for the bookstore
    #lets have three threads for each of the services
 
    
     order_status_response = {
        "orderId": order_id,
        "status": "Order Approved",
        # "suggestedBooks": parse_suggested_books(suggested_books_json)
     }
    #   "suggestedBooks": [
    #         {"bookId": "123", "title": "The Best Book", "author": "Author 1"},
    #         {"bookId": "456", "title": "The Second Best Book", "author": "Author 2"},
    #     ],

    return order_status_response


if __name__ == "__main__":
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host="0.0.0.0")
