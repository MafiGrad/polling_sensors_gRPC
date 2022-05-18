from concurrent import futures
from turtle import position

import grpc
import try_protos_pb2
import try_protos_pb2_grpc

class Sensors(try_protos_pb2_grpc.SensorsServicer):
    
    def RelayState(self, request, context):
        print(f"I have a request from {request.name}. Relay count {request.count}. Positions {request.position}.")
        return try_protos_pb2.RelayResponse(name="OrangePi Zero One", state=request.count+request.position)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    try_protos_pb2_grpc.add_SensorsServicer_to_server(Sensors(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()