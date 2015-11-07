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

def averageList(l):
	return sum(l)/float(len(l))

class entry(ndb.Model):
	def __init__(
		self,
		courseCode=None,
		professor=None,
		grade=None,
		profReview=None,
		courseReview=None,
		courseRating=None,
		profRating=None):

		self.courseCode = courseCode
		self.professor = professor
		self.grade = grade
		self.profReview = profReview
		self.courseReview = courseReview
		self.courseRating = courseRating
		self.profRating = profRating
		date = ndb.DateTimeProperty(auto_now_add=True)

		entryDict.append(self)

		def printEntry(self):
			print("Course:",self.coursecode)
			print("Professor:",self.professor)
			print("Professor Rating:",self.profRating)
			print("Course Rating:",self.courseRating)
			print("Professor Review:",self.profReview)
			print("Course Review:",self.courseReview)
			print("Course:",self.coursecode)


class retrieveData():
	def __init__(self,category,subobject):
		self.entryList = []
		for entry in entryDictionary:
			if entry.retrieveCategory == subobject:
				entryList.append(entry)

	def averageGrade(self):
		gradeList = [entry.grade for entry in self.entryList]
		return

	def averageProfRating(self):
		ratingList = [entry.profRating for entry in self.entryList]
		return averageList(ratingList)

	def averageCourseRating(self):
		ratingList = [entry.courseRating for entry in self.entryList]
		return averageList(ratingList)

class Post(ndb.Model):
    courseCode = ndb.StringProperty(required=True)
    year = ndb.StringProperty(required=True)
	professor = ndb.StringProperty(required=True)
	grade = ndb.StringProperty(required=True)
    courseReview = ndb.TextProperty(required=True)
	professorReview = ndb.TextProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        # Get all of the student data from the datastore
        query = Post.query()
        post_data = query.fetch()
        # Pass the data to the template
        template_values = {
            'posts' : post_data
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Get the student name and university from the form
		courseCode = self.request.get('course')
		year = self.request.get('year')
		professor = self.request.get('professor_name')
		grade = self.request.get('grade')
		courseReview = self.request.get('course_review')
		professorReview = self.request.get('professor_review')
        # Create a new Student and put it in the datastore
        post = Post(course=course, year=year, professor=professor, grade=grade, courseReview=courseReview, professorReview = professorReview)
        post.put()
        # Redirect to the main handler that will render the template
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/about', AboutHandler),
    ('/forum', ForumHandler),
    ('/showposts', CommentHandler),
    # ('/showposts', ShowpostsHandler)
], debug=True)
