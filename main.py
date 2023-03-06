import string
from random import randint, random, choice
from concurrent import futures
import json
import grpc
import prot_pb2
import prot_pb2_grpc


def rstring():
    letters = string.ascii_letters
    return ''.join(choice(letters) for _ in range(randint(3, 10)))


def datatype(level, keys):
    t = randint(0, 6 - (level == 0) * 2)  # for every 7 type in json, if level is 0, then types are 5
    if t == 0:
        return rstring()
    elif t == 1:
        return randint(-255, 256)
    elif t == 2:
        return random() * randint(-255, 256)
    elif t == 3:
        return randint(0, 1) == 1
    elif t == 4:
        return None
    elif t == 5:
        return create_json(level - 1, keys)
    elif t == 6:
        return [create_json(level - 1, keys) for _ in range(randint(0, 5))]


def create_json(level, keys):
    n_of_keys = randint(0, len(keys))
    js = {}
    for i in range(n_of_keys):
        cur_key = keys[randint(0, len(keys))]
        js[cur_key] = datatype(level, keys)
    return js


class Myserver(prot_pb2_grpc.Myserver):
    def GetKeys(self, request, context):
        print("Get Keys")
        js = json.loads(str(request.json))
        a = [i for i in js]
        s = json.dumps(json.JSONEncoder().encode(a))
        reply = prot_pb2.Simple_Json_Reply(json=s)
        return reply

    def GenerateJson(self, request, context):
        print("Generate Json")
        js = create_json(request.level, [rstring() for _ in range(request.numkeys)])
        print(js)
        s = json.dumps( json.JSONEncoder.encode(js) )
        reply = prot_pb2.Simple_Json_Reply(json=s)
        return

    def FindValue(self, request, context):
        return super().FindValue(self, request, context)

    def Convert(self, request, context):
        return super().Convert(self, request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prot_pb2_grpc.add_MyserverServicer_to_server(Myserver(), server)
    server.add_insecure_port("localhost:50050")
    server.start()
    server.wait_for_termination()


serve()
