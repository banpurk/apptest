import webapp2
import os
import jinja2

class MainPage(webapp2.RequestHandler):
  def get(self):
        self.response.out.write(html)
    
  def post(self):
        Compliance = self.request.get("Compliance")
        Workload = self.request.get("Workload")
        self.response.out.write("Compliance selected: " + Compliance + " Workload selected: " + Workload)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
