#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This script is a bit ass first so apologies before you start.

script is constructed in the handler class and handed in all relevent arguments. 
Logs the user in with details supplied with the config file
naviages tot he correct page
inserts the questions, answers, marks and other information.

Does not handle exceptions well!
if the plugins that handle the quizzes get updated there is a good chance 
that it will not work.
"""

import time
import importConfig
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Insert:
	question = ''
	answer_array = []
	URL = ''
	category = ''
	correct_answer_info = ''
	
	def __init__(self, ques, answers, url, category, answerInfo):
		self.questionText = ques.decode("utf-8")
		self.answer_array = answers
		self.correct_answer_info = answerInfo.decode("utf-8")
		self.categoryname = category.decode("utf-8")
		self.URL = url.decode("utf-8")
		

		
	def insert(self):

		driver = webdriver.Firefox()
		#Login to the wordpress backend
		driver.get("http://cope.kitson-consulting.co.uk/wp-admin/")
		username = driver.find_element_by_id('user_login')
		username.send_keys(importConfig.user)
		password = driver.find_element_by_id('user_pass')
		password.send_keys(importConfig.password)
		password.send_keys(Keys.RETURN)
		time.sleep(4) #wait for the page to respond
		
				
		#go to the correct url where questions can be uploaded
		driver.get(self.URL)

		#Enter the name of the question
		question = driver.find_element_by_id('question_name')

		questionText = self.questionText
		question.send_keys(questionText)
		counter = 1
		"""With one of the updates all of these changed and itt broke the script.
		If any of these do not work check the terminal for a warning that it couldn't find
		a element with id or class = blah. Then come here and change it to the new class/id name"""
		for x in range(len(self.answer_array)):
			driver.find_element_by_id('new_answer_button').click()
			question = driver.find_element_by_id('answer_{}'.format(counter))
			answer = self.answer_array[x][0]
			question.send_keys(answer)
			
			driver.find_element_by_id('answer_{}_points'.format(counter)).clear()
			
			driver.find_element_by_id('answer_{}_points'.format(counter)).send_keys(self.answer_array[x][1])
			if self.answer_array[x][1] == '1':
				driver.find_element_by_id('answer_{}_correct'.format(counter)).click()
				
			counter += 1
			
		driver.find_element_by_id('correct_answer_info').send_keys(self.correct_answer_info)
		#ensure that the category name does not have any spaces in it. Otherwise the 
		#category id will be id='category name' and it fails to find it
		catName = self.categoryname.replace(' ', '_')
		
		driver.find_element_by_id('new_category{}'.format(catName)).click()
		driver.find_element_by_css_selector('form.question_form > input.button-primary').click()
		
		time.sleep(1)
		driver.close()
		



