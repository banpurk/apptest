import webapp2

html = """
<!doctype html>
<html>
        <head>
                This is a form to pick compliance and workload 
        </head>
        <body>
                <form method="post">
                        <label for= "Compliance">Compliance:</label>
                        <input name="Compliance" type="text" value=""><br>
                
                        <label for= "Workload">Workoad:</label>
                        <input name="Workload" type="text" value=""><br>
                
                        <input name="" type="submit" value="Submit">
                </form>
        </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
        self.response.out.write(html)
    
  def post(self):
        self.response.out.write("Compliance selected: " + Compliance + "Workload selected: " + Workload)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
