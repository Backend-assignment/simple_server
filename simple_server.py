#Import libraries for server
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
        #handle GET command
        def do_GET(self):
            self.send_response(200)
    
            self.send_header('Content-type','text-html')
            self.end_headers()
    
            #Send message back to client
            message = "Hello world!"
            #Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            return

def run():
    print('starting server...')
    
    #Server settings
    #Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8080)

    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
