from wsgiref.simple_server import  make_server


def app(env, res):
    print env
    res_body = "<h1>Welcome to WSGI server</h1>"

    status = '200 OK'
    res_header = [('Content-Type', 'text/html')]
    res(status, res_header)

    return [res_body]

httpd = make_server('localhost', 8080, app)
#httpd.handle_request()
httpd.serve_forever()