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
entryDict = []
# Define a Post model for the Datastore
class Post(ndb.Model):
	courseCode = ndb.StringProperty(required=True)
	year = ndb.StringProperty(required=True)
	professor = ndb.StringProperty(required=True)
	grade = ndb.StringProperty(required=True)
	courseReview = ndb.TextProperty(required=True)
	professorReview = ndb.TextProperty(required=True)
	date = ndb.DateTimeProperty(auto_now_add=True)


class SuccessfulHandler(webapp2.RequestHandler):
    def get(self):
        query = Post.query()
        post_data = query.fetch()
        # Pass the data to the template
        template_values = {
            'course_posts' : post_data
        }
        template = JINJA_ENVIRONMENT.get_template('addsuccessful.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Get the student name and university from the form
        courseCode = self.request.get('courseCode')
        year = self.request.get('year')
        professor = self.request.get('professor')
        grade = self.request.get('grade')
        courseReview = self.request.get('courseReview')
        professorReview = self.request.get('professorReview')
        # Create a new Student and put it in the datastore
        post = Post(courseCode=courseCode, year=year, professor=professor, grade=grade, courseReview=courseReview, professorReview = professorReview)

        post.put()
        # Redirect to the main handler that will render the template
        self.redirect('/successful')

class CommentHandler(webapp2.RequestHandler):
    def get(self):
        # Get all of the student data from the datastore
        post_key = ndb.Key(urlsafe=url_string)
        shown_post = post_key.get()
        shown_post.put()

        shown_post_array = [shown_post]
        # Pass the data to the template
        template_values = {
            'posts' : shown_post_array
        }
        template = JINJA_ENVIRONMENT.get_template('forum.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Create the comment in the Database
        name = self.request.get('name')
        comment = self.request.get('comment')


        # Find the post that was commented on using the hidden post_url_key
        post_url_key = self.request.get('post_url_key')
        post_key = ndb.Key(urlsafe=post_url_key)
        post = post_key.get()

        # Attach the comment to that post
        post.comment_keys.append(comment_key)
        post.put()

        self.redirect('/forum?id=' + post.key.urlsafe())

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
	('/successful', SuccessfulHandler),
	('/forum', CommentHandler),
	], debug=True)
