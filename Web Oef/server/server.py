from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process()

    def do_POST(self):
        self.process()

    def process(self):
        content_length=0
        if self.headers["Content-Length"]:
            content_length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(content_length).decode("utf-8") 
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        data = "<h1>path</h1><pre>"  + str(self.path) + "</pre>"
        data = data + "<h1>request-body</h1> "  + request_body + "</pre>"
        data = data + "<h1>request-headers</h1><pre>"  + str(self.headers)  + "</pre>"
        self.wfile.write(bytes(data, "utf8"))
 

with HTTPServer(("", 8001), handler) as server:
    server.serve_forever()
