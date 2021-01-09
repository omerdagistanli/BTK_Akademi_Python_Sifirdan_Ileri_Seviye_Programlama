from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "omerdagistanli96"
password = "omrdgstn1996"

class Github():
    def __init__(self,username,password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]").click()

        time.sleep(1)

        code = input("Gmaile gelen kodu girin:")

        self.browser.find_element_by_xpath("//*[@id='otp']").send_keys(code)
        self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[3]/form/button").click()

        time.sleep(1)

# class Gmail():
#     def __init__(self):
#         self.browser = webdriver.Firefox()
#         self.username = "omerdagistanli1996@gmail.com"
#         self.password = "sunguroqlu"
#
#     def signIn(self):
#         self.browser.get("https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=AddSession")
#         time.sleep(2)
#
#         self.browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(self.username)
#         self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
#         time.sleep(2)
#
#         self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(self.password)
#         self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
#         time.sleep(2)

github = Github(username, password)
github.signIn()

# gmail = Gmail()
# gmail.signIn()