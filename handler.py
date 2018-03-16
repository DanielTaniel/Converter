#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

This handler will read the CSV and supply the insertQuestion script with the inputs
it requires to add questsions

Example of url to upload when using this script
https://cope.kitson-consulting.co.uk/wp-admin/admin.php?page=mlw_quiz_options&quiz_id=8

The config file has all of the cope login details so do not include it if you are using git

The CSV must have no new lines, these were causing responses to be split into different groups
The Category name must have no spaces
The csv will require | as a delimiter, other delimiters were being used in the file and causing the 
script to add additional rows to the array.
There may be some issues with non ascii characters when the forign language translations come through.

"""

import insertQuestion
import csv
import sys
import codecs

question = ""
answers = []
URL = sys.argv[1]
answerInfo = ''
category = ''
results = []
questionData = []



first = True


with codecs.open('questions.csv', 'rb', encoding='utf-8') as reader:
	for row in reader:
		if first: 
			first = False
			continue
			
		else:	
			results.append(row.encode('utf-8').split("|"))
			

	
for y in results:
	print(y)
	answers = []
	category = y[0]
	question = y[1]
	answerInfo = y[2]
	print(category)
	print(question)
	print(answerInfo)
	i = 3
	while i < len(y):
		if y[i] != '' and y[i+1] != '':
			answers.append([y[i].decode('utf-8'), y[i+1].decode('utf-8')])
		i+=2
	#insert question expects the questions as a string, 
	#the answers in an array an the form (Question, answer), (question2, answer2)...
	#URL of the page when questions can be uploaded
	#Category (this must be with no spaces as it defines the html class selected
	#if the class has a space it will not find the correct class
	#and answerinfo which is a string. 
	insert = insertQuestion.Insert(question, answers, URL, category, answerInfo)
	insert.insert()
