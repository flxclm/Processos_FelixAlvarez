from http.server import  BaseHTTPRequestHandler, HTTPServer

class http_server:
    def __init__(self):
        server = HTTPServer(('', 8080), myHandler)
        server.serve_forever()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path.endswith('.jpg'):
            f = open('image.jpg')
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        else:
            self.send_error(404, "Page not found")

        return

class main:
    def __init__(self):

        self.server = http_server()

if __name__ == '__main__':
    m = main()
