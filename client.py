import json

import grpc
import prot_pb2
import prot_pb2_grpc

with grpc.insecure_channel('localhost:50050') as channel:
    stub = prot_pb2_grpc.MyserverStub(channel)
    # list_request = input().split('?')
    # op = list_request[0]
    op = "/find"
    if op == "/generate":
        f = open('client_data.json')
        request = prot_pb2.Keys_Request(json=json.dumps(json.load(f)))
        f.close()
        print(json.loads(stub.GetKeys(request).json))

    elif op == "/generate":
        request = prot_pb2.Generate_Request(level=1, numkeys=3)
        print(json.loads(stub.GenerateJson(request).json))
        pass
    elif op == "/find":
        f = open('client_data.json')
        request = prot_pb2.Find_Request(json=json.dumps(json.load(f)), value="spoon")
        f.close()
        print(json.loads(stub.FindValue(request).json))
        pass
