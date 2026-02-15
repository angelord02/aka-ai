import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'dashboard/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

print(f"Démarrage du dashboard sur http://localhost:{PORT}")
print("Vous pouvez suivre mon travail en direct via ce lien (en environnement supporté).")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.serve_forever()
