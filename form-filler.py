#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
form-filler.py

Created on Mon Jul  5 13:00:38 2021

@author: andrew gross, adopted from 
https://towardsdatascience.com/using-python-and-selenium-to-automate-filling-forms-and-mouse-clicks-f87c74ed5c0f
by Melvin Fernandez
"""

###############################################################################
### Import Modules
###############################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import pandas

###############################################################################
### Import Files & Paths
###############################################################################
chromedriver_location = "/home/andrew/Programs/chromedriver"
formData = pandas.read_csv('/home/andrew/Data/Python/form-filler/inputs.csv')

###############################################################################
## Case 0: Test case
###############################################################################
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.instagram.com/')

first_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_input = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input'
login_submit = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div'

driver.find_element_by_xpath(first_login).click()
driver.find_element_by_xpath(first_login).send_keys('\t')
driver.send_keys('\t')
driver.send_keys('username')

driver.find_element_by_xpath(first_login).send_keys('username')

###############################################################################
## Case 1: Thermo Fisher, xpath
###############################################################################
driver = webdriver.Chrome(chromedriver_location)
driver.get("http://www.python.org")
driver.get('https://jobs.thermofisher.com/global/en/job/166635BR/Quality-Assurance-Engineer')
driver.get('')
driver.get('https://jobs.thermofisher.com/global/en/job/166528BR/Engineer-II-Manufacturing')
driver.get('https://jobs.thermofisher.com/global/en/job/166823BR/Field-Applications-Engineer-II-PA-NJ-NY')
driver.get('https://jobs.thermofisher.com/global/en/job/163480BR/Data-Engineer')
driver.get('https://jobs.thermofisher.com/global/en/job/168087BR/Systems-Verification-and-Validation-Engineer-Scientist-II')

###############################################################################
# 1.1 - Apply on the listing page
# 1.1.1 - Log in
signup = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div/a/span'
signup = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div/a/span'
signin = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div[2]/div[2]/div/div[2]/div[3]/a'
signinemail = '//*[@id="signinEmail"]'
pword = '//*[@id="signInPassword"]'
signinbutton = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div[2]/div[2]/div/div[1]/div[3]/form/div/div[4]/div[1]/button'
pwordInput = formData.iloc[0,3]

## If not logged in
driver.find_element_by_xpath(signup).click()
driver.find_element_by_xpath(signup).send_keys('Keys.ENTER')

### CLEAN THIS UP!!
#element = driver.find_element_by_xpath(signup)
#driver.execute_script("arguments[0].click();", element)

driver.find_element_by_xpath(signin).click()
driver.find_element_by_xpath(signinemail).send_keys('andrew.reginald.gross@gmail.com')
driver.find_element_by_xpath(pword).click()
driver.find_element_by_xpath(pword).send_keys(pwordInput)
driver.find_element_by_xpath(signinbutton).click()


apply = '/html/body/div[2]/div[2]/div/div[1]/div[2]/section[3]/div/div/div/div[2]/a'
apply = '/html/body/div[2]/div[2]/div/div[1]/div[2]/section[3]/div/div/div/div[2]/a/ppc-content'

tfemployee = '//*[@id="thermoFisherEmployee"]'
tfworker = '//*[@id="thermoFisherWorker"]'
affiliates = '//*[@id="thermoFisherAffiliates"]'
email = '//*[@id="username"]'
continue1 = '//*[@id="page1a"]'

driver.find_element_by_xpath(apply).click()

###############################################################################
## 1.2 - First page: TF employee check
driver.find_element_by_xpath(tfemployee).send_keys('N')
driver.find_element_by_xpath(tfworker).send_keys('N')
driver.find_element_by_xpath(affiliates).send_keys('N')
#driver.find_element_by_xpath(email).send_keys('andrew.reginald.gross@gmail.com')
driver.find_element_by_xpath(continue1).click()

###############################################################################
## 1.3 - 2nd page - Region, ethnicity, disability status
region = '//*[@id="region"]'
apac = '//*[@id="apacAgreement"]'
vet = '//*[@id="veteran"]'
name = '//*[@id="name"]'
gender = '//*[@id="gender"]'
ethnicity = '//*[@id="ethnicity"]'
disability = '//*[@id="disability"]'
yourName = '//*[@id="yourName"]'
submit = '//*[@id="submit"]'

driver.find_element_by_xpath(region).send_keys('U')
driver.find_element_by_xpath(apac).send_keys('A')
driver.find_element_by_xpath(vet).send_keys('N')
driver.find_element_by_xpath(name).send_keys('Andrew Gross')
driver.find_element_by_xpath(gender).send_keys('M')
driver.find_element_by_xpath(ethnicity).send_keys('C')
driver.find_element_by_xpath(disability).send_keys('I')
driver.find_element_by_xpath(yourName).send_keys('Andrew Gross')
driver.find_element_by_xpath(submit).click()

###############################################################################
## 1.4 - 3rd page - Resume import
linkedin_signin = '/html/body/div[1]/div[2]/button/span'
# //*[@id="awli-button-member-logged-out"]/span
# /html/body/div[1]/div[2]/button/span
linkedin_apply = '//*[@id="awli-button-member-1625550301074"]/span'
country = '//*[@id="country"]'
state = '//*[@id="state"]'
city = '//*[@id="city"]'
zipcode = '//*[@id="zipCode"]'
phone = '//*[@id="phoneNumber"]'
website = '//*[@id="webAddress"]'
firstname = '//*[@id="preferredFirstName"]'
lastname = '//*[@id="preferredLastName"]'
continue2 = '//*[@id="submit"]'

### LINKEDIN SIGN IN

## This isn't working
element = driver.find_element_by_xpath(linkedin_signin)
element = driver.find_element_by_css('/html/body/div[1]/div[2]/button/span')
driver.execute_script("arguments[0].click();", element)

driver.find_element_by_xpath(linkedin_signin).click()
driver.find_element_by_xpath(linkedin_apply).click()
driver.find_element_by_xpath(country).send_keys('United States')
driver.find_element_by_xpath(state).send_keys('Ca')
driver.find_element_by_xpath(city).send_keys('Los Angeles')
driver.find_element_by_xpath(zipcode).send_keys('90018')
driver.find_element_by_xpath(phone).send_keys('4126575332')
driver.find_element_by_xpath(website).send_keys('https://www.linkedin.com/in/andrew-r-gross/')
driver.find_element_by_xpath(firstname).send_keys('Andrew')
driver.find_element_by_xpath(lastname).send_keys('Gross')
driver.find_element_by_xpath(continue2).click()

###############################################################################
## 1.5 - 4th page - Experience
## Experience
driver.find_element_by_xpath(submit).click()


###############################################################################
## 1.6 - 5th page - Education
gradyear = '//*[@id="graduationYear"]'
degree = '//*[@id="degree"]'
aos1 = '//*[@id="areaOfStudy"]'
gradyear1 = '//*[@id="graduationYear1"]'
degree1 = '//*[@id="degree1"]'
aos2 = '//*[@id="areaOfStudy1"]'

driver.find_element_by_xpath(gradyear).send_keys('10-2014')
driver.find_element_by_xpath(degree).send_keys('M')
driver.find_element_by_xpath(aos1).send_keys('Biology')
driver.find_element_by_xpath(gradyear1).send_keys('05-2010')
driver.find_element_by_xpath(degree1).send_keys('B')
driver.find_element_by_xpath(aos2).send_keys('Chemical Engineering')
driver.find_element_by_xpath(submit).click()

###############################################################################
## 1.7 - 6th page - Cover Letter
cletter = '//*[@id="attachmentsClassification"]'
addfile = '//*[@id="uploadCoverLetter"]/div/label/message'
submit = '//*[@id="submit"]'

driver.find_element_by_xpath(cletter).send_keys('Cover')
driver.find_element_by_xpath(addfile).click()
#driver.find_element_by_xpath(addfile).send_keys('CoverLetter-Illumina.pdf')
driver.find_element_by_xpath(submit).click()

###############################################################################
## 1.8 - 6th page - How did you hear?
source = '//*[@id="source"]'
submit = '//*[@id="submit"]'

driver.find_element_by_xpath(source).send_keys('Thermo Fisher Website')
driver.find_element_by_xpath(submit).click()

###############################################################################
## 1.9 - 6th page - More questions
question1 = '//*[@id="question1"]'
question2 = '//*[@id="question2"]'
question3 = '//*[@id="question3"]'
question4 = '//*[@id="question4"]'
question5 = '//*[@id="question5"]'
question6 = '//*[@id="question6"]'
driver.find_element_by_xpath(question1).send_keys('N')
driver.find_element_by_xpath(question2).send_keys('N')
driver.find_element_by_xpath(question3).send_keys('N')
driver.find_element_by_xpath(question4).send_keys('N')
driver.find_element_by_xpath(question5).send_keys('Y')
driver.find_element_by_xpath(question6).send_keys('N')

### SUBMIT TO COMPLETE!
driver.find_element_by_xpath(submit).click()


