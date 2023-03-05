import socketserver
import json


def parse_operation(a):
    return a[0].split(' ')[1][2::].split('=')[0]


def parse_values(a):
    return a[0].split(' ')[1].split('=')[1], a[0].split(' ')[1].split('=')[2]


def parse_values(a):
    return a[0].split(' ')[1].split('=')[1]


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(":)")
        a = str(self.request.recv(1024).strip(), "utf-8").split('\n')

        op = parse_operation(a)

        if op == "keys":
            y = json.loads(a[-1])
            a = {}
            for i in y:
                a[i] = ""
            #TODO: HTTP answer
            self.request.sendall(bytes("???", "utf-8"))

        elif op == "generate?level":
            level, numkeys = parse_values(a)
            # TODO:
        elif op == "find?value":
            value = parse_values(a)
            # TODO:
        elif op == "convert":
            pass
            # TODO:


server = socketserver.TCPServer(('127.0.0.5', 8000), Myserver)

print("is running")
server.serve_forever()
# server.server_close()
# print("server dead")
