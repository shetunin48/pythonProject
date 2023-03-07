import io
from pydub import AudioSegment
from concurrent import futures
import grpc
from protos import prot_pb2
import prot_pb2_grpc
from consts import MAX_MESSAGE_LENGTH
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
        js = find_value(request.json, request.value)
        print(js)
        reply = prot_pb2.Simple_Json_Reply(json=js)
        return reply

    def Convert(self, request, context):
        print("Convert")
        f = io.BytesIO(request.base64)
        flac_audio = AudioSegment.from_file(f, format="flac")
        flac_audio.export("music.mp3", format="mp3")

        f = open('music.mp3', 'rb')
        data = f.read()
        f.close()
        reply = prot_pb2.Convert_Reply(base64=data)
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])

    prot_pb2_grpc.add_MyserverServicer_to_server(Myserver(), server)
    server.add_insecure_port("localhost:50050")
    server.start()
    print("Server started")
    server.wait_for_termination()
    print("Server terminated")


serve()
