

import os
import webapp2
import jinja2
from google.appengine.ext import ndb
import urllib
from google.appengine.api import urlfetch


entryDict = []

def averageList(l):
	return sum(l)/float(len(l))

class entry:
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




