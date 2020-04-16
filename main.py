import webapp2
import os
import jinja2
import urllib
import json
import cloudstorage
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.cloud import storage

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
     #   self.response.write(user)
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
    
  ''' def post(self):
    storage_client = storage.Client()
    bucket = storage_client.bucket("divine-engine-270122.appspot.com")
#    blob = bucket.blob("job-1")
    filename = '/{}/job-1'.format(bucket)
    with cloudstorage.open(filename, 'w') as filehandle:
            filehandle.write(json.dumps({"god": "great"}))
    
    template = JINJA_ENVIRONMENT.get_template('congrats.html')
    self.response.write(template.render())'''

app = webapp2.WSGIApplication([('/', Login), 
                               ('/home', MainPage)], debug= True)
