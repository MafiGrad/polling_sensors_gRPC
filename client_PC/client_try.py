import grpc
import try_protos_pb2
import try_protos_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = try_protos_pb2_grpc.SensorsStub(channel)
        response = stub.RelayState(try_protos_pb2.RelayRequest(name="PC Client", count=8,position=10))
    print(f"States on {response.name} is: {response.state}")

if __name__ == '__main__':
    run()