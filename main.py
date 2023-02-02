from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import logging 
#from Logs_extract import extract_incoming_logs

#HOST = "192.168.1.185"
HOST = "localhost"
PORT = 8080
log_file = "C:\\Users\\ailias\\Desktop\\ServerIncoming_Sever_logs.txt"

class NeuralHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(bytes("<html><body><h1> Hello World!</h1></body></html>", 
                               "utf-8"))
        logging.basicConfig(format='%(asctime)s - %(message)s!!!')
        logging.info("This is a info message")
        
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "'+ date + '"}', "utf-8"))
        #extract_incoming_logs(log_file)

        
        
server = HTTPServer((HOST,PORT), NeuralHTTP)
print("Server is now running")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print ("Server stopped")