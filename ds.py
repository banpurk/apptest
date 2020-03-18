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
    
