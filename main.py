from concurrent import futures
import json
import grpc
import prot_pb2
import prot_pb2_grpc
from rjson import generate_json, get_keys, find_value


class Myserver(prot_pb2_grpc.Myserver):
    def GetKeys(self, request, context):
        print("Get Keys")
        js = get_keys(request.json)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def GenerateJson(self, request, context):
        print("Generate Json")
        js = generate_json(request.level, request.numkeys)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def FindValue(self, request, context):
        print("Find Value")
        js = find_value(request.level, request.numkeys)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def Convert(self, request, context):
        return super().Convert(self, request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prot_pb2_grpc.add_MyserverServicer_to_server(Myserver(), server)
    server.add_insecure_port("localhost:50050")
    server.start()
    print("Server started")
    server.wait_for_termination()
    print("Server terminated")


serve()
