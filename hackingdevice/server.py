import grpc
from concurrent import futures
import api_pb2
import api_pb2_grpc

class HackingDeviceServer(api_pb2_grpc.HackingDeviceServerServicer):
    def read_secret_station_data(self, request, context):
        print("📡 Secret data request received!")
        return api_pb2.SecretStationDataResponse(
            data=["Station Alpha: OK", "Station Beta: ⚠️ Power fluctuation", "Station Gamma: Offline 🚫"]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_HackingDeviceServerServicer_to_server(HackingDeviceServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🛰️ Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()