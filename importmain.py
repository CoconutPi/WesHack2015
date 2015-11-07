import os
import webapp2
import jinja2
from google.appengine.ext import ndb
import urllib
from google.appengine.api import urlfetch


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Define a Post model for the Datastore
class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    author = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    comment_keys = ndb.KeyProperty(kind='Comment', repeated=True)

class Comment(ndb.Model):
    name = ndb.StringProperty(required=True)
    comment = ndb.TextProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

class ForumHandler(webapp2.RequestHandler):
    def get(self):
        # Get all of the student data from the datastore
        query = Post.query()
        post_data = query.fetch()
        # Pass the data to the template
        template_values = {
            'posts' : post_data
        }
        template = JINJA_ENVIRONMENT.get_template('forum.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Get the student name and university from the form
        title = self.request.get('title')
        content = self.request.get('content')
        author = self.request.get('author')
        # Create a new Student and put it in the datastore
        post = Post(title=title, content=content, author=author)
        post.put()
        # Redirect to the main handler that will render the template
        self.redirect('/forum')
