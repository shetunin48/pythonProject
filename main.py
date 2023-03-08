import io
import os
import sys

from pydub import AudioSegment
from concurrent import futures
import grpc

import prot_pb2
import prot_pb2_grpc
from consts import MAX_MESSAGE_LENGTH, DEFAULT_URL
from rjson import generate_json, get_keys, find_value


class Myserver(prot_pb2_grpc.MyserverServicer):
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
        js = find_value(request.json, request.value)
        print(js)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def Convert(self, request, context):
        print("Convert")
        f = io.BytesIO(request.base64)
        flac_audio = AudioSegment.from_file(f, format=request.audioformat)
        flac_audio.export("./tmp/music.mp3", format="mp3", bitrate="320k")

        f = open("./tmp/music.mp3", "rb")
        data = f.read()
        f.close()
        os.remove("./tmp/music.mp3")

        reply = prot_pb2.Convert_Reply(base64=data)
        return reply


def serve(url):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])

    prot_pb2_grpc.add_MyserverServicer_to_server(Myserver(), server)
    server.add_insecure_port(url)
    server.start()
    print("Server started")
    server.wait_for_termination()
    print("Server terminated")


url = DEFAULT_URL
if ("-h" in sys.argv) or len(sys.argv) == 1:
    print("\n-------------------------------------------\n"
          "This is grpc server for parsing json objects and converting audio files.\n\n"
          "use --url <ip:port> to open server at this url (default is ", DEFAULT_URL, ")"
          "\n-------------------------------------------\n")

if "--url" in sys.argv:
    url = sys.argv[sys.argv.index("--url") + 1]

serve(url)
