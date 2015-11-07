
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

courseDictionary = {}
html = htmlGet("https://iasext.wesleyan.edu/regprod/!wesmaps_page.html")
for line in range(len(html)):
	textLine = html[line]
	if courseIndicator in textLine:

		beginLink = textLine.find(courseIndicator)
		endLink = textLine.find("\">")
		extension = textLine[beginLink:endLink]
		link = defaultPage + extension

		beginName = endLink+2
		endName = textLine.find("</a><br>")
		name = textLine[beginName:endName]

		code = link[65:69]

		courseDictionary[code] = (name,link)


		#print(link)
		#print(name)
		#print(code)
		#print line,html[line]
for i in courseDictionary:
	print(i)



"https://iasext.wesleyan.edu/regprod/"

print(len(courseIndicator))

courseDictionary = {}


