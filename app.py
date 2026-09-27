from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from cloudhost PaaS test deploy!\n')
HTTPServer(('0.0.0.0', 8080), H).serve_forever()
