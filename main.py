import webapp2

html = """
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
                
                <input name="" type="submit" value="">
        </form>
        </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.right(html)
    
  def post(self):
    self.response.out.right("Compliance selected: " + compliance 
                           + "Workload selected: " + workload)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
