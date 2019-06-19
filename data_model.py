from google.appengine.ext import ndb
import datetime

class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required = True)
#    date = ndb.DateTimeProperty(required = True)
