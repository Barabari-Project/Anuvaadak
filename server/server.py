#!/usr/bin/env python
"""./dummy-web-server.py -l localhost -p 3000
Send a POST request: curl -d "foo=bar&bin=baz" http://localhost:3000
"""
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pywhisper import main as whisper

model = "small"
isHTML = True

# link = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"
# result = main(link, model)
# print(result)


class S(BaseHTTPRequestHandler):
    def _set_headers(self, html):
        self.send_response(200)
        if html:
            self.send_header('Content-type', 'text/html')
        else:
            self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)

        content = self._html("Are you sure this is what you needed?")

        if self.path.startswith('/anuvaad'):
            isHTML = False
            content = bytes(str(query), 'utf8')

        self._set_headers(isHTML)
        self.wfile.write(content)

    def do_HEAD(self):
        self._set_headers(isHTML)

    def do_POST(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)
        print(query)

        self._set_headers(isHTML)
        self.wfile.write(self._html("POST!"))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=3000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=3000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
