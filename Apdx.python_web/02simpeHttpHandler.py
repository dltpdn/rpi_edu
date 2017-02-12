#ref : https://docs.python.org/2/library/simplehttpserver.html#module-SimpleHTTPServer
import SimpleHTTPServer
import SocketServer

PORT = 8080
httpd = SocketServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

print "server on%d" %PORT
httpd.serve_forever()