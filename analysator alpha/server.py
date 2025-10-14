import grpc
from concurrent import futures
import time
import api_pb2
import api_pb2_grpc
from pymongo import MongoClient

client = MongoClient('mongodb://theship:theship1234@127.0.0.1:2021/theshipdb')
db = client.theshipdb
collection = db["vacuum-energy"]

class SensorVoidEnergyServer(api_pb2_grpc.SensorVoidEnergyServerServicer):
    def read_sensor_data(self, request, context):
        data_object = collection.find_one({})
        return api_pb2.SensorData(hexdata=data_object["data"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_SensorVoidEnergyServerServicer_to_server(SensorVoidEnergyServer(), server)
    server.add_insecure_port('[::]:2102')  # Listening on port 2102
    server.start()
    print("Server is running on port 2102...")
    
    try:
        while True:
            time.sleep(86400)  # Keep the server alive
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()