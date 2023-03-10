import io
import json
import os
import sys
from pydub import AudioSegment
from concurrent import futures
import grpc

import consts
import prot_pb2
import prot_pb2_grpc
from consts import MAX_MESSAGE_LENGTH, DEFAULT_URL
from rjson import generate_json, get_keys, find_value
import google.protobuf.message
import threading

sem = threading.Semaphore(value=1)


class Myserver(prot_pb2_grpc.MyserverServicer):
    flag_for_msg = False

    def Test(self, request, context):
        print("???")
        print(request.DESCRIPTOR.fields_by_name.keys())
        return prot_pb2.Array_Reply(arr=request.DESCRIPTOR.fields_by_name.keys())

    def GetKeys(self, request, context):
        print("Get Keys")
        print(request.json)
        js = get_keys(request.json)
        reply = prot_pb2.Array_Reply(arr=js)
        return reply

    def GenerateJson(self, request, context):
        print("Generate Json")
        print(request.level, request.numkeys)
        js = generate_json(request.level, request.numkeys)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def FindValue(self, request, context):
        print("Find Value")
        print(request.json, request.value)
        js = find_value(request.json, request.value)
        reply = prot_pb2.Array_Reply(arr=js)
        return reply

    def Convert(self, request, context):
        if self.flag_for_msg:
            print("busy")
            reply = prot_pb2.Convert_Reply(base64=bytes(), message="Server is busy")
            return reply

        sem.acquire()
        self.flag_for_msg = True
        print("Convert")

        f = io.BytesIO(request.base64)
        flac_audio = AudioSegment.from_file(f, format=request.audioformat)
        flac_audio.export("/tmp/music.mp3", format="mp3", bitrate="320k")

        f = open("/tmp/music.mp3", "rb")
        data = f.read()
        f.close()
        os.remove("/tmp/music.mp3")

        self.flag_for_msg = False
        sem.release()
        reply = prot_pb2.Convert_Reply(base64=data, message="successfully")
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


def main():
    url = DEFAULT_URL
    if ("-h" in sys.argv) or len(sys.argv) == 1:
        print("\n------------------------------------------------------------------------------\n"
              "This is grpc server for parsing json objects and converting audio files.\n\n"
              "use --url <ip:port> to open server at this url (default is ", DEFAULT_URL, ")"
                                                                                          "\n------------------------------------------------------------------------------\n")

    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]

    #if "--start" in sys.argv:
    serve(url)


main()
