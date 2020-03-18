from protorpc import messages
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

class Compliance(messages.Enum):
    GDPR = 0
    PCI = 1
    HIPPA = 2

class Workload(messages.Enum):
    Warehouse = 0
    DLP = 1
    
class compwork(ndb.Model):
    """A main model for representing an individual entry."""
    compliance = msgprop.EnumProperty(Compliance, required=True)
    workload = msgprop.EnumProperty(Workload, required=True)
    
class Datastore(webapp2.RequestHandler):

def post(self):
    print("Hello")
    guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
    greeting = Greeting(parent=guestbook_key(guestbook_name))

    if users.get_current_user():
       greeting.author = Author(
           identity=users.get_current_user().user_id(),
           email=users.get_current_user().email())

       greeting.content = self.request.get('content')
       greeting.put()

       query_params = {'guestbook_name': guestbook_name}
       self.redirect('/?' + urllib.urlencode(query_params))
