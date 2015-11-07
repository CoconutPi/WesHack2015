
from string import *
from random import *
from webbrowser import *
from urllib import *
from urllib2 import *
from time import *
import os
import pwd
from zlib import *
import platform
import sys



browserVersion = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'

courseIndicator = "!wesmaps_page.html?subj_page="

defaultPage = "https://iasext.wesleyan.edu/regprod/"

def zlibDecode(data):
	return decompress(data, 16 + MAX_WBITS)

def parse(code):
	codeString = ""
	codeList = []
	length = len(code)
	for index in range(length):
		i = code[index]
		if i != "":
			codeString += i
		if i == "\n":
			codeList.append(codeString)
			codeString = ""
	return(codeList)

def htmlGet(url):
	try:
		request = Request(url, headers={'User-Agent': browserVersion})
		response = urlopen(request).read()
	except None:
		return htmlGet(url)
	code = response
	try:
		code = zlibDecode(code)
	except error:
		pass
	codeList = parse(code)
	return codeList

def download(link,File):
	#print(File)
	#print(link)
	print("It's here")
	Mozilla.retrieve(link,File)
	return None

class departmentDict:
	def __init__(self):
		self.dict = {}

		self.html = htmlGet("https://iasext.wesleyan.edu/regprod/!wesmaps_page.html")
		for line in range(len(self.html)):
			self.textLine = self.html[line]
			if courseIndicator in self.textLine:
		
				self.beginLink = self.textLine.find(courseIndicator)
				self.endLink = self.textLine.find("\">")
				self.extension = self.textLine[self.beginLink:self.endLink]
				self.link = defaultPage + self.extension

				self.beginName = self.endLink+2
				self.endName = self.textLine.find("</a><br>")
				self.name = self.textLine[self.beginName:self.endName]

				self.endCode = 65 + self.link[65:].find("&")

				self.code = self.link[65:self.endCode]

				self.dict[self.code] = (self.name,self.link)

class courseDict:
	
	def __init__(self,departmentCode):
		self.set = set()

		self.link = "https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?crse_list=" + departmentCode.upper() + "&term=1159&offered=Y"
		html = htmlGet(self.link)
		for line in html:
			if "<a href=\"" in line:
				self.beginCode = line.find("\">")+2
				line = line[self.beginCode:]
				self.endCode = line.find("-")
				code = line[:self.endCode]
				self.set.add(code)

		self.link = "https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?crse_list=" + departmentCode.upper() + "&term=1159&offered=N"
		html = htmlGet(self.link)
		for line in html:
			if "<a href=\"" in line:
				self.beginCode = line.find("\">")+2
				line = line[self.beginCode:]
				self.endCode = line.find("</a>")
				code = line[:self.endCode]
				self.set.add(code)


#Just run this function to get the list of every courses offered at Wesleyan. It takes one minute to retrieve this data through airwes.
#This function returns a one dimensional list.
def getCourseList():
	courseList = []
	for i in departmentDict().dict:
		print "Retrieving course",i
		clist = courseDict(i)
		for j in clist.set:
			courseList.append(j)

	courseList = list(set(courseList))
	return courseList







		
