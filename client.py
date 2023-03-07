import json

import grpc
from protos import prot_pb2
import prot_pb2_grpc
from consts import MAX_MESSAGE_LENGTH

with grpc.insecure_channel('localhost:50050', options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)]) as channel:
    stub = prot_pb2_grpc.MyserverStub(channel)
    # list_request = input().split('?')
    # op = list_request[0]
    op = "/convert"
    if op == "/keys":
        f = open('client_data.json')
        request = prot_pb2.Keys_Request(json=json.dumps(json.load(f)))
        f.close()
        print(json.loads(stub.GetKeys(request).json))

    elif op == "/generate":
        request = prot_pb2.Generate_Request(level=1, numkeys=3)
        print(json.loads(stub.GenerateJson(request).json))
    elif op == "/find":
        f = open('client_data.json')
        request = prot_pb2.Find_Request(json=json.dumps(json.load(f)), value="Betelgeusian")
        f.close()
        print(json.loads(stub.FindValue(request).json))
    elif op == "/convert":
        f = open('music.flac', 'rb')
        data = f.read()
        f.close()
        request = prot_pb2.Convert_Request(audioformat="flac", base64=data)
        stub.Convert(request)
