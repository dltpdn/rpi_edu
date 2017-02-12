import BaseHTTPServer
import SocketServer


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>Helo! Welcome to My Simple Server</h1>')
        return


PORT = 8080
httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "server on%d" %PORT
httpd.serve_forever()