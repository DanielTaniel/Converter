#!/usr/bin/python
# -*- coding: utf-8 -*-

import insertQuestion
import csv
import sys
import codecs

print ("Pass in the url of the page contain the quiz as an argument")

question = ""
answers = []
URL = sys.argv[1]
answerInfo = ''
category = ''

results = []
questionData = []


"""
https://cope.kitson-consulting.co.uk/wp-admin/admin.php?page=mlw_quiz_options&quiz_id=8

"""
first = True


with codecs.open('demo2.csv', 'rb', encoding='utf-8') as reader:
	for row in reader:
		if first: 
			first = False
			continue
			
		else:	
			results.append(row.encode('utf-8').split(","))
			
for y in results:
	answers = []
	category = y[0]
	question = y[1]
	answerInfo = y[2]
	print(category)
	print(question)
	print(answerInfo)
	for i in xrange(3, 13, 2):
		if y[i] is not '' and y[i+1] is not '':
			answers.append([y[i].decode('utf-8'), y[i+1].decode('utf-8')])
	insert = insertQuestion.Insert(question, answers, URL, category, answerInfo)
	insert.insert()
	"""
	for x in answers:
		print ('Answers = ')
		print(x)
	answers = []
	results = []
#print(results)
#print( category)
#print(question)
#print(answerInfo)

"""
