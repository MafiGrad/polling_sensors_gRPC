from concurrent import futures

import grpc
import try_protos_pb2
import try_protos_pb2_grpc

class Sensors(try_protos_pb2_grpc.SensorsServicer):
    
    def RelayState(self, request, context):
        print(f"I have a request from {request.name}. Relay count {request.count}. Positions {request.position}.")
        return try_protos_pb2.RelayResponse(name="OrangePi Zero One", state=request.count+request.position)

def serve(address: str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    try_protos_pb2_grpc.add_SensorsServicer_to_server(Sensors(), server)
    server.add_insecure_port(address)
    server.start()
    print(f"Server started on adress {address}")
    server.wait_for_termination()

def main():
    serve('[::]:50051')

if __name__ == '__main__':
    main()