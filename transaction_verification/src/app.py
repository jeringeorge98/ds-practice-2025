import sys
import os
import uuid
import random
import time
# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
transaction_verification_grpc_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/bookstore/transaction_verification'))
sys.path.insert(0, transaction_verification_grpc_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc
import grpc
from concurrent import futures


class TransactionVerificationService(transaction_verification.TransactionVerificationService):
    def VerifyTransaction(self, request, context):
        """
        Dummy implementation of the VerifyTransaction method
        Takes a transaction request and returns a response indicating whether the transaction is valid
        """
        print(f"Received transaction verification request for order ID: {request.order_id}, user ID: {request.user_id}")
        response = transaction_verification.TransactionVerificationResponse()
        response.is_valid = True
        response.message = "Transaction verified successfully"
        time.sleep(10)
        return response
    
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add FraudDetectionService
    transaction_verification_grpc.add_TransactionVerificationServiceServicer_to_server(TransactionVerificationService(), server)
    # Listen on port 50051
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Transaction Server started. Listening on port 50051.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
     serve()  