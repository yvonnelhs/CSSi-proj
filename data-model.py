from google.appengine.ext import ndb

class Post(ndb.model):
    title = ndb.StringProperty(required=True)
    description = ndb.DateTimeProperty(required=True)
    link = ndb.StringProperty(required = False)
