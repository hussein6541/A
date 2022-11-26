# -*- coding: utf-8 -*-
#@adowat Baron Team
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
hostName = "localhost"
serverPort = 8080
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        baron=open("هنا مسار صفحة html ","r")
        baron=baron.read()
        self.wfile.write(bytes( baron,"utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()