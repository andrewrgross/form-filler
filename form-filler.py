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
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime

### Too dangerous!
'''
from pynput.keyboard import Key, Controller
keyboard = Controller()
keyboard.press(Key.alt_l)
keyboard.press('/t')
keyboard.release('/t')
keyboard.release(Key.alt_l)
keyboard.press('c')
keyboard.release('c')
keyboard.type('Nitratine')
'''

###############################################################################
### Import Files & Paths
###############################################################################
chromedriver_location = "/home/andrew/Programs/chromedriver"
formData = pd.read_csv('/home/andrew/Data/Python/form-filler/inputs.csv')

### Define functions
def make_interactable(target,key_to_send):
    element = wait.until(EC.presence_of_element_located((By.XPATH, target)))
    actionChains = ActionChains(driver)
    actionChains.move_to_element(element).click().perform()
    actionChains.move_to_element(element).send_keys(key_to_send).perform()

###############################################################################
## Case 0: Test case
###############################################################################
driver = webdriver.Chrome(chromedriver_location)
driver = webdriver.Chrome(chromedriver_location, chrome_options=options)

driver.get('https://www.instagram.com/')

first_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_input = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input'
login_submit = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div'

driver.find_element_by_xpath(first_login).click()
driver.find_element_by_xpath(first_login).send_keys('\t')
driver.send_keys('\t')
driver.send_keys('username')

driver.find_element_by_xpath(first_login).send_keys('username')

actions = ActionChains(driver)
actions.send_keys('dummydata')
actions.perform()



















###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
## Case 1: Thermo Fisher
###############################################################################
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://jobs.thermofisher.com/')

###############################################################################
# 1.1 - Apply on the listing page
# 1.1.1 - Log in
signup = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div/a/span'
signin = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div[2]/div[2]/div/div[2]/div[3]/a'
signinemail = '//*[@id="signinEmail"]'
pword = '//*[@id="signInPassword"]'
signinbutton = '/html/body/div[1]/section[2]/div/div/header/div/div/div[3]/nav/ul/li[8]/section/div/div/div[2]/div[2]/div/div[1]/div[3]/form/div/div[4]/div[1]/button'
pwordInput = formData.iloc[0,3]

## If not logged in
driver.find_element_by_xpath(signup).click()
driver.find_element_by_xpath(signup).send_keys('Keys.ENTER')

driver.find_element_by_xpath(signin).click()
driver.find_element_by_xpath(signinemail).send_keys('andrew.reginald.gross@gmail.com')
driver.find_element_by_xpath(pword).click()
driver.find_element_by_xpath(pword).send_keys(pwordInput)
driver.find_element_by_xpath(signinbutton).click()

apply = '/html/body/div[2]/div[2]/div/div[1]/div[2]/section[3]/div/div/div/div[2]/a'
#apply = '/html/body/div[2]/div[2]/div/div[1]/div[2]/section[3]/div/div/div/div[2]/a/ppc-content'

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

### LINKEDIN SIGN IN: requires user to click a pop-up
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





















###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
## Case 2: Edwards Lifesciences
###############################################################################
driver = webdriver.Chrome(chromedriver_location, chrome_options=options)
driver.get("https://edwards.wd5.myworkdayjobs.com/edwardscareers/14/refreshFacet/318c8bb6f553100021d223d9780d30be")
driver.get('https://edwards.wd5.myworkdayjobs.com/edwardscareers')

###############################################################################
## 2.1 - Sign in
signin = '//*[@id="wd-Authentication-NO_METADATA_ID-uid118"]/button/span[2]'
email = '//*[@id="vpsBody"]/div[6]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/input'
pword = '//*[@id="vpsBody"]/div[6]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/input'
pwordInput = formData.iloc[0,3]
signinbutton = '//*[@id="vpsBody"]/div[6]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div'

driver.find_element_by_xpath(signin).click()
driver.find_element_by_xpath(email).click()
driver.find_element_by_xpath(email).send_keys('andrew.reginald.gross@gmail.com')
driver.find_element_by_xpath(pword).click()
driver.find_element_by_xpath(pword).send_keys(pwordInput)
driver.find_element_by_xpath(signinbutton).click()

###############################################################################
## 2.1.1 - Select previous resume
nextButton = '//*[@id="1a993b45b9374a63a2fb89996e0490a7"]/span[2]'
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 2.2 - Employee check & referal
ref = '/html/body/div[4]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/div'
ref2= '/html/body/div[4]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[2]/div/div'
driver.find_element_by_xpath(ref).click()
actions.send_keys('j',Keys.RETURN).perform()

nextButton = '/html/body/div[4]/div[1]/div[1]/section/div[2]/div[2]/div[2]/button[1]/span[2]'
nextButton = '//*[@id="00a1d4ed8fd5422bb9f07809b03bf71b"]/span[2]'
nextButton = '//*[@id="ef530aaa90524f5e9f1c56d7d41d62ed"]/span[2]'
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 2.3 - Work Experience
nextButton = '/html/body/div[4]/div[1]/div[1]/section/div[2]/div[2]/div[2]/button[1]/span[2]'
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 2.4 - Application Questions
age = '/html/body/div[4]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li/div[2]/div/div/div[1]/div'

driver.find_element_by_xpath(age).click()
actions = ActionChains(driver)
actions.pause(0.5)
actions.send_keys('y')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys('y')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys('n')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys('y')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys('n')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.2)
actions.send_keys('n')
actions.pause(0.2)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys('120000')
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.RETURN)
actions.perform()

###############################################################################
## 2.5 - Personal Information

gender = '/html/body/div[4]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/ul/li/div[2]/div/div/div[1]/div'

driver.find_element_by_xpath(gender).click()
actions = ActionChains(driver)
actions.pause(0.5)
actions.send_keys('m')
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys('n')
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys('w')
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(1)
actions.send_keys(' ')
actions.pause(0.5)

actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.RETURN)
actions.perform()

###############################################################################
## 2.6 - Voluntary Self-Identification of Disibility
name = '/html/body/div[4]/div[1]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/ul[1]/li[4]/div[2]/div/div/input'

driver.find_element_by_xpath(name).send_keys('Andrew Gross')

actions = ActionChains(driver)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(datetime.date.today().month)
actions.pause(0.5)
actions.send_keys(datetime.date.today().day)
actions.pause(0.5)
actions.send_keys(datetime.date.today().year)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(' ')
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.RETURN)
actions.perform()

###############################################################################
## 2.7 - Manually click "Submit"






















###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
## Case 3: Johnson & Johnson
###############################################################################
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://jobs.jnj.com/auth/1/login")
#driver.get("https://www.careers.jnj.com/")

###############################################################################
## 3.1 - Sign in

email = '//*[@id="mat-input-0"]'
pword = '//*[@id="mat-input-1"]'
emailInput = formData.iloc[0,2]
pwordInput = formData.iloc[0,3]
signinbutton = '//*[@id="all-content"]/div[2]/login-module/login-shared-container/ojl-login-component/form/button'

#make_interactable(email, 'python')
driver.find_element_by_xpath(email).send_keys(emailInput)
driver.find_element_by_xpath(pword).send_keys(pwordInput)
driver.find_element_by_xpath(signinbutton).click()

###############################################################################
## 3.2 - Search and apply

searchField = '//*[@id="keyword-search"]'
#searchField = '//*[@id="ContextLocationSearch-keywords"]'
locationField = '//*[@id="location-search"]'
searchButton = '//*[@id="searchBarContainer"]/search-bar/div/form/div[2]/button[2]/span[1]/span'
sortBy = '//*[@id="selected-item"]'
posted = '//*[@id="mat-option-296"]/span'

#make_interactable(searchField, 'python')
driver.find_element_by_xpath(searchField).send_keys('python')
driver.find_element_by_xpath(locationField).send_keys('California')
driver.find_element_by_xpath(searchButton).click()

driver.find_element_by_xpath(sortBy).click()
driver.find_element_by_xpath(posted).click()

### Manually select job and click "Apply"

driver.find_element_by_xpath(email).send_keys(emailInput)
driver.find_element_by_xpath(pword).send_keys(pwordInput)
driver.find_element_by_xpath(signinbutton).click()

###############################################################################
## 3.2 - Select Resume

selFromPrevButton = '//*[@id="all-content"]/div[2]/div[2]/div/apply-app/job-component/q-question-container/div/form/div[1]/div/div/div/div/div/q-question-resolver/div/q-flow-component/div/q-upload-component/div[3]/div[1]/button/span'
uploadButton = '//*[@id="preview-upload"]/q-upload-buttons/button'
nextButton = '//*[@id="button-next-question"]'
driver.find_element_by_xpath(selFromPrevButton).click()
driver.find_element_by_xpath(uploadButton).click()
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 3.2 - Select Cover Letter
driver.find_element_by_xpath(nextButton).click()
driver.find_element_by_xpath(selFromPrevButton).click()
driver.find_element_by_xpath(uploadButton).click()
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 3.3 - Personal Information

driver.find_element_by_xpath(nextButton).click()
driver.find_element_by_xpath(nextButton).click()
driver.find_element_by_xpath(nextButton).click()

###############################################################################
## 3.4 - Questions

driver.find_element_by_xpath(nextButton).click()
driver.find_element_by_xpath(nextButton).click()
driver.find_element_by_xpath(nextButton).click()

### Here, manually answer any necessary questions and click "Next"

###############################################################################
## 3.5 - EEO Questions
### Click at the top of the page

actions = ActionChains(driver)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(' ')
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys('w')
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(' ')
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.RETURN)
actions.perform()

###############################################################################
## 3.6 - Voluntary self identification of disbility

### Click at the top of the page

actions = ActionChains(driver)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(' ')
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.DOWN)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys('Andrew R Gross')
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(1)
actions.send_keys(Keys.TAB)
actions.pause(0.5)
actions.send_keys(' ')
actions.pause(1)
actions.send_keys(Keys.RETURN)
actions.perform()


### Then, manually click "Submit"














###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
## Case 4: 
###############################################################################
driver = webdriver.Chrome(chromedriver_location, chrome_options=options)
driver.get('')








