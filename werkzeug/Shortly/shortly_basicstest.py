#!/usr/bin/env python

#WSGI base application
def application_wsgi(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ["Hello World"]

from werkzeug.wrappers import Response,Request

def application(environ,start_response):
    request = Request(environ)
    text = "Hello %s!"% request.args.get('name','World')
    response = Response(text,mimetype='text\plain')
    return response(environ,start_response) 

if __name__ =='__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4002, application,use_reloader=True)