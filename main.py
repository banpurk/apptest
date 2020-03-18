import webapp2
import os
import jinja2

class MainPage(webapp2.RequestHandler):
  def get(self):
        template_values = {
            'Compliance': Compliance,
            'Workload': Workload,
        }
      
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    
  def post(self):
        Compliance = self.request.get("Compliance")
        Workload = self.request.get("Workload")
        self.response.out.write("Compliance selected: " + Compliance + " Workload selected: " + Workload)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
