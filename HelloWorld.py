import webapp2

form ="""
        <form method ='post'>
                What's your DOB?
                <br>
                <label>Month
                    <input type="text" name = "month"/>
                </label>
                <label>DATE
                    <input type="text" name = "date"/>
                </label>
                <label>YEAR
                    <input type="text" name = "year"/>
                </label>
                <br>
                <input type="submit" />   
        </form>
       """
MONTHS=['January',
        'Febuary',
        'March',
        'April'
        'May'
        'June'
        'July'
        'August'
        'September'
        'October'
        'November'
        'December']

month_abbvs = dict((m[:3].lower(),m) for m in MONTHS)

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
        
    def post(self):
        self.response.out.write("Thanks for that totally valid date")
        
    def valid_Month(self,month):
        returnval = None

        if month:
            if len(month)==3 and month.lower() in month_abbvs:
                month = month_abbvs(month.lower())
            elif month.capitalize() in MONTHS:
                returnval = month.capitalize()
        return returnval


app = webapp2.WSGIApplication([('/', HelloWebapp2)],
                                     debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app,host='localhost',port ='8080')
#    run_wsgi_app(application)

if __name__ == "__main__":
    main()