import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler


class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "idk1")
        self.send_header("idk2", "idk3")
        self.end_headers()


server = HTTPServer(('', 8000), Myserver)

print("is running")
server.serve_forever()
server.server_close()
print("server dead")
