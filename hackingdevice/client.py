import grpc
import api_pb2
import api_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = api_pb2_grpc.HackingDeviceServerStub(channel)
        response = stub.read_secret_station_data(api_pb2.Void())
        print("💾 Secret data received:")
        for entry in response.data:
            print(" -", entry)

if __name__ == "__main__":
    main()