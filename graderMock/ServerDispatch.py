# -*- coding: utf-8 -*-

import socketserver
from http.server import BaseHTTPRequestHandler
import json
import GraderMock
import RecievedFileParser

print('File starts')

PORT = 10801

class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print('POST Handled')
        if self.path == '/pass_task':
            content_length = int(self.headers['Content-Length'])
            task_text = RecievedFileParser.parseFile(self.rfile, content_length)
            user_email = self.headers['email']
            graded_result = GraderMock.validate_task(task_text, user_email)
            self.send_response(200, 'OK')
            self.send_header('content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(graded_result).encode('utf-8'))
        else:
            self.send_response(404, 'not found!')
            self.send_header('content-type', 'text/html')
            self.end_headers()

    def do_GET(self):
        self.send_response(404, 'not found!')


httpd = socketserver.TCPServer(("", PORT), HTTPHandler)
print('Api is alive ^_^')
httpd.serve_forever()
