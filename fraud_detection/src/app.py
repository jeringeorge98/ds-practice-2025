import sys
import os
import uuid
import random
import time
# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
fraud_detection_grpc_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/bookstore/fraud_detection'))
sys.path.insert(0, fraud_detection_grpc_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

import grpc
from concurrent import futures

# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.FraudDetectionServiceServicer
class FraudDetectionService(fraud_detection_grpc.FraudDetectionServiceServicer):
    # Create an RPC function to say hello
    def SayHello(self, request, context):
        # Create a HelloResponse object
        response = fraud_detection.FraudDetectionResponse()
        # Set the greeting field of the response object
        response.is_fraudulent = False
        response.risk_score = 0.1
        response.review_id = "hello-" + str(uuid.uuid4())
        
        # Print the response for debugging
        print(f"Hello response: {response}")
        # Return the response object
        return response
    
    def DetectUserFraud(self, request, context):
        """
        Dummy implementation of the DetectUserFraud method
        Takes user order info and returns a response indicating whether the order is fraudulent
        """
        print(f"Received fraud detection request for order ID: {request.order_id}, user ID: {request.user_id}")
        
        # Create response object
        response = fraud_detection.FraudDetectionResponse()
        
        # For demo purposes, generate a random result
        # In a real implementation, you would analyze user behavior patterns
        is_fraud = random.random() < 0.2  # 20% chance of being flagged as fraud
        
        # Set response fields
        response.is_fraudulent = is_fraud
        response.risk_score = random.uniform(0.0, 0.8) if not is_fraud else random.uniform(0.8, 1.0)
        response.review_id = f"review-{uuid.uuid4()}"
        
        print(f"Fraud detection result: {response}")
        time.sleep(5)
        return response
    
    def DetectCreditCardFraud(self, request, context):
        """
        Dummy implementation of the DetectCreditCardFraud method
        Takes order info and returns a response indicating whether the credit card use is fraudulent
        """
        print(f"Received credit card fraud detection request for order ID: {request.order_id}")
        
        # Create response object
        response = fraud_detection.FraudDetectionResponse()
        
        # For demo purposes, generate a random result
        # In a real implementation, you would analyze credit card usage patterns
        is_fraud = random.random() < 0.1  # 10% chance of being flagged as fraud
        
        # Set response fields
        response.is_fraudulent = is_fraud
        response.risk_score = random.uniform(0.0, 0.7) if not is_fraud else random.uniform(0.7, 1.0)
        response.review_id = f"cc-review-{uuid.uuid4()}"
        
        print(f"Credit card fraud detection result: {response}")
        return response
   
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add FraudDetectionService
    fraud_detection_grpc.add_FraudDetectionServiceServicer_to_server(FraudDetectionService(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Fraud Detection Server started. Listening on port 50051.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()