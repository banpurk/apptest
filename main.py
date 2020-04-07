import webapp2
import os
import jinja2
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

class Entry(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    compliance= ndb.StringProperty(indexed=False)
    workload = ndb.StringProperty(indexed=False)

class Login(webapp2.RequestHandler):
  def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }
      
        template = JINJA_ENVIRONMENT.get_template('sample.html')
        self.response.write(template.render(template_values))
        
class MainPage(webapp2.RequestHandler):
   def get(self):
        Compliance = str(self.request.get("Compliance"))
        Workload = str(self.request.get("Workload"))
        template_values = {
            'Compliance': Compliance,
            'Workload': Workload,
        }
      
        template = JINJA_ENVIRONMENT.get_template('new.html')
        self.response.write(template.render(template_values))
    
   def post(self):
        entry = Entry()
        entry.compliance = self.request.get("Compliance")
        entry.workload = self.request.get("Workload")
        entry.put()
      #  template_values = {'a':'HELLO'}
        template = JINJA_ENVIRONMENT.list_templates()
        self.response.write(template)
      #  self.response.write(template.render())y

app = webapp2.WSGIApplication([('/', Login), 
                               ('/home', MainPage)], debug= True)
  
