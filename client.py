import json
import sys
import grpc

import prot_pb2
import prot_pb2_grpc
from consts import MAX_MESSAGE_LENGTH


def try_open(ind, how="r"):
    try:
        return open(sys.argv[ind + 1], how)
    except FileNotFoundError:
        print("Couldn't open file")
        sys.exit(-1)
    except FileExistsError:
        print("Couldn't open file")
        sys.exit(-1)


def client():
    if ("-h" in sys.argv) or len(sys.argv) == 1:
        print("\n-------------------------------------------\n"
              "use --keys <path to json> to get a json array of all keys in json object\n"
              "use --generate <level> <numkeys> to generate random json\n"
              "use --find <name of json file> <value> to find all keys in json with the same value\n"
              "use --convert <name of music file> <name for new mp3> to convert it to mp3\n\n"
              "use --file <name of file> to write result in file\n\n"
              "use --url <ip:port> for address of connection\n"
              "-------------------------------------------\n")
        return

    url = '127.0.0.1:50050'
    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]

    with grpc.insecure_channel(url, options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)]) as channel:
        stub = prot_pb2_grpc.MyserverStub(channel)

        file_out = sys.stdout

        if "--file" in sys.argv:
            ind = sys.argv.index("--file")
            file_out = try_open(ind)

        if "--keys" in sys.argv:
            ind = sys.argv.index("--keys")
            f = try_open(ind)
            request = prot_pb2.Keys_Request(json=json.dumps(json.load(f)))
            f.close()
            print(stub.GetKeys(request).arr, file=file_out)

        elif "--generate" in sys.argv:
            ind = sys.argv.index("--generate")
            request = prot_pb2.Generate_Request(level=int(sys.argv[ind + 1]), numkeys=int(sys.argv[ind + 2]))
            print(stub.GenerateJson(request).json, file=file_out)

        elif "--find" in sys.argv:
            ind = sys.argv.index("--find")
            f = try_open(ind)
            request = prot_pb2.Find_Request(json=json.dumps(json.load(f)), value=sys.argv[ind + 2])
            f.close()
            print(stub.FindValue(request).arr, file=file_out)

        elif "--convert" in sys.argv:
            ind = sys.argv.index("--convert")
            f = try_open(ind, 'rb')
            data = f.read()
            f.close()

            request = prot_pb2.Convert_Request(audioformat=(sys.argv[ind + 1].split('.')[-1]), base64=data)
            file_out = try_open(ind + 1, 'wb')
            file_out.write(stub.Convert(request).base64)

        file_out.close()


client()
