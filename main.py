import os
import webapp2
import jinja2
from data_model import Post
import json
from google.appengine.api import users
from datetime import datetime

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#print(Post.query())

    #f=open(date.strftime('(%Y-%m-%d %H:%M:%S %Z)')+title+".html","w+")

def isPostThere(post):
    for i in range(len(Post.query().fetch())):
        if Post.query().fetch()[i].title== post.title:
            if Post.query().fetch()[i].link== post.link:
                if Post.query().fetch()[i].message== post.message:
                    if Post.query().fetch()[i].date== post.date:
                        return True
    return False

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home = the_jinja_env.get_template('templates/homepage.html')
        self.response.write(home.render())
    def post(self):
        home = the_jinja_env.get_template('templates/homepage.html')
        self.response.write(home.render())

class AboutUs(webapp2.RequestHandler):
    def get(self):
        about = the_jinja_env.get_template('templates/aboutUs.html')
        self.response.write(about.render())

class LogIn(webapp2.RequestHandler):
    def get(self):
        login_url=users.create_login_url("/")
        self.redirect(login_url)

class AddFakeNews(webapp2.RequestHandler):
    def get(self):
        addnews = the_jinja_env.get_template('templates/addFakeNews.html')
        self.response.write(addnews.render())
    def post(self):
        postresults = the_jinja_env.get_template('templates/homepage.html')
        fakenews_title = self.request.get('title')
        fakenews_link = self.request.get('link')
        fakenews_message = self.request.get('message')

        fakenews = Post(
            title = fakenews_title,
            message = fakenews_message,
            link = fakenews_link
        )
        fakenews.put()
        while(isPostThere(fakenews)==False):
            pass
        #f=open(fakenews_title+".html","w+")
        #f.write("")
        print("done")


        dict = {
           "fakeNewsLink": fakenews_link,
           "fakeNewsMessage": fakenews_message,
           "fakeNewsTitle": fakenews_title
        }

        self.response.write(postresults.render(dict))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/aboutus', AboutUs),
    ('/login', LogIn),
    ('/addfakenews', AddFakeNews)
    #('/fakenews/(\w+)', RenderFakeNews)
], debug = True)
