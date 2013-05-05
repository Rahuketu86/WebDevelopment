import webapp2

form ="""
        <form method ='post' action="/testform">
                <!-- action where a form submits to -->
                <select name = 'q'>
                    <option>one</option>
                    <option>two</option>
                    <option>three</option>
                </select>
                <br>
                <!-- Submits the form which by default submit to itself--></-->
                <input type="submit" />
                
            </form>
        """
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
        
class TestHandler(webapp2.RequestHandler):
    def post(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#         q = self.request.get("q")
#         self.response.out.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', HelloWebapp2),
                               ('/testform',TestHandler)],
                                     debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app,host='localhost',port ='8080')
#    run_wsgi_app(application)

if __name__ == "__main__":
    main()