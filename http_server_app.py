import http.server
import os

class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px; '><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>","utf-8"))
        self.wfile.close
        
        if __name__== "__main__":
            server = http.server.HTTPServer(('localhost','5000'), HandleRequests)
            server.serve_forever()
