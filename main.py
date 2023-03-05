import socketserver
import json


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(":)")

        a = str(self.request.recv(1024).strip(), "utf-8").split('\n')
        print(a[-1])


server = socketserver.TCPServer(('127.0.0.5', 8000), Myserver)

print("is running")
server.serve_forever()
server.server_close()
print("server dead")
