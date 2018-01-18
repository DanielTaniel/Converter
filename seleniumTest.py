#!/usr/bin/python
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

answer_array = [["answer1", 1, 1], ["answer2", 0, 0], ["answer3", 0, 0]]
correct_answer_info = "This is some correct answer info"
categoryname = "Team Working"
URL = 'https://cope.kitson-consulting.co.uk/wp-admin/admin.php?page=mlw_quiz_options&quiz_id=8'
driver = webdriver.Firefox()
#Login to the wordpress backend
driver.get("http://cope.kitson-consulting.co.uk/wp-admin/")
username = driver.find_element_by_id('user_login')
username.send_keys("ccw_admin")
password = driver.find_element_by_id('user_pass')
password.send_keys("rp(1B!^)6I)AeQJf6M4tAVZ^")
password.send_keys(Keys.RETURN)

time.sleep(4) #wait for the page to respond
#go to the correct url
driver.get(URL)

#Enter the name of the question
question = driver.find_element_by_id('question_name')

question.send_keys('This is a test')
counter = 1
for x in range(len(answer_array)):
	driver.find_element_by_id('new_answer_button').click()
	question = driver.find_element_by_id('answer_{}'.format(counter))
	question.send_keys(x)
	
	if answer_array[x][1] is 1:
		print(answer_array[x][0])
		print(answer_array[x][1])
		print('answer_{}_correct'.format(counter))
		driver.find_element_by_id('answer_{}_correct'.format(counter)).click()
		driver.find_element_by_id('answer_{}_points'.format(counter)).send_keys(answer_array[x][2])
	
	counter += 1
	
driver.find_element_by_id('correct_answer_info').send_keys(correct_answer_info)

driver.find_element_by_id('new_category{}'.format(categoryname)).click()
driver.find_element_by_css_selector('form.question_form > input.button-primary').click()



