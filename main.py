from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import logging 
import sys
sys.path.append('C:\\Users\\ailias\\Desktop\\XM_project\\XM_Technical_Task')
import Site_body as sb

#HOST = "192.168.1.185"
HOST = "localhost"
PORT = 9999
#log_file = "ServerIncoming_Sever_logs.txt"
#logging.basicConfig(filename='test.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
#logging.basicConfig(filename='test.log', level=logging.INFO)

class NeuralHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(sb.Html_site('HTML_Site.txt'), "utf-8"))
        
    def do_GET2(self):

        if ola_komple:
            self.wfile.write(bytes("QIFSA", "utf-8"))
            self.send_response(200)
        else: 
            self.send_response(404)
            self.send_error({"Error":"Not found"})
            
        
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "'+ date + '"}', "utf-8"))
     
                   


        
server = HTTPServer((HOST,PORT), NeuralHTTP)
print("Server is now running")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print ("Server stopped")