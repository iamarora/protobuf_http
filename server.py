#!/usr/bin/python

import BaseHTTPServer
import json
import threading
import time
import person_pb2 as proto

TIMEOUT_IN_SECONDS = 10
TEST_CALL = '''curl --header "Content-Type: application/json" --request POST --data '{"name":"Ankit","id":1}' http://localhost:1111'''
persons = []


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print post_data
        if 'name' in post_data and 'id' in post_data:
            post_data = json.loads(post_data)
            person = proto.Person(id=post_data['id'], name=post_data['name'])
            persons.append(person)
            response = 'Saved to protobuf'
        else:
            response = 'Please call api with post data eg: {}'.format(TEST_CALL)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response)


def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=Handler):
    server_address = ('localhost', 1111)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def flush_to_disk():
    global persons
    print('Rolling over file', persons)
    if persons:
        with open('persons_{}.pb'.format(time.time()), 'wb+') as f:
            for p in persons:
                f.write(p.SerializeToString())
        persons = []
    threading.Timer(TIMEOUT_IN_SECONDS, flush_to_disk).start()

try:
    flush_to_disk()
except KeyboardInterrupt:
    sys.exit(0)

run()

