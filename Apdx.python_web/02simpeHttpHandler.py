#ref : https://docs.python.org/2/library/simplehttpserver.html#module-SimpleHTTPServer
import http.server
import socketserver

PORT = 8080
httpd = socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler)

print("server on%d" %PORT)
httpd.serve_forever()