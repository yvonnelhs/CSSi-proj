import os
import webapp2
import jinja2
from google.appengine.api import users
from data_model import Post

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def isNewer(a,b):
    #print (Post.query().fetch()[i].date.strftime('%Y-%m-%d %H:%M:%S %Z'))
    if (int(a.date.strftime('%Y'))>=int(b.date.strftime('%Y'))):
        if (int(a.date.strftime('%m'))>=int(b.date.strftime('%m'))):
            if (int(a.date.strftime('%d'))>=int(b.date.strftime('%d'))):
                if (int(a.date.strftime('%H'))>=int(b.date.strftime('%H'))):
                    if (int(a.date.strftime('%M'))>=int(b.date.strftime('%M'))):
                        if (int(a.date.strftime('%S'))>=int(b.date.strftime('%S'))):
                            return True
    return False

def isAscending(list):
    for i in range(len(list)-1):
        if(isNewer(list[i],list[i+1])==False):
            return False
    return True

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #self.response.write("To be or not to be")
            self.redirect("/loggedin")

        else:
            #self.response.write("You are not logged in!")
            self.redirect("/nouser")


class NoUserHandler(webapp2.RequestHandler):
    def get(self):

        login_url = users.create_login_url("/")
        self.response.write('Please log in. <a href = "' + login_url + '">Login here</a>')

class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/homepage')

class HomePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        username = user.nickname()
        logout_url = users.create_logout_url("/")
        self.response.write("Hello " + username + '. You are logged in. <a href = "' + logout_url + '">Click here to logout</a>')


        home = the_jinja_env.get_template('templates/homepage.html')
        self.response.write(home.render())

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

        for i in range(len(Post.query().fetch())):
            print (Post.query().fetch()[i].date.strftime('%Y-%m-%d %H:%M:%S %Z'))
        print(Post.query().fetch()[0],Post.query().fetch()[1].date)
        print(isNewer(Post.query().fetch()[0],Post.query().fetch()[1]))
        #sort by latest to earliest
        listofPosts=Post.query().fetch()
        while(isAscending(listofPosts)==False):
            for i in range(len(listofPosts)-1):
                if(isNewer(listofPosts[i],listofPosts[i+1])):
                    x=listofPosts[i]
                    listofPosts[i]=listofPosts[i+1]
                    listofPosts[i+1]=x


        dict = {
            "fakeNewsLink": fakenews_link,
            "fakeNewsMessage": fakenews_message,
            "fakeNewsTitle": fakenews_title
        }
        self.response.write(postresults.render(dict))






class AddFakeNews(webapp2.RequestHandler): #/addFakeNews
    def get(self):
        self.redirect("/homepage")
    def post(self):
        addFakeNews = the_jinja_env.get_template('templates/addFakeNews.html')
        self.response.write(addFakeNews.render())













class NewsResults(webapp2.RequestHandler):
    pass

class AboutUs(webapp2.RequestHandler):
    def get(self):
        about = the_jinja_env.get_template('templates/aboutUs.html')
        self.response.write(about.render())





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/loggedin', LoggedInHandler),
    ('/nouser', NoUserHandler),
    ('newsresults', NewsResults),
    ('/homepage', HomePage),
    ('/addFakeNews', AddFakeNews),
    ('/aboutus', AboutUs),
], debug = True)
