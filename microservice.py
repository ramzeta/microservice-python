import json
from wsgiref.simple_server import make_server

def application(environ,start_response):
    headers = [('Content-type', 'application/json')]

    start_response('200 ok',headers)

    response = {
        'message' :'hello world in this service'
    }

    return bytes(json.dumps(response), 'utf-8')

server = make_server('localhost',8080, application)
server.handle_request()
