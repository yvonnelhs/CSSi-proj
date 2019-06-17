from google.appengine.ext import ndb
from google.appengine.ext import users

class User(ndb.model):
    username=ndb.StringProperty(required=True)
    birthday=ndb.DateTimeProperty(required=True)
    
