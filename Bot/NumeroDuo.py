from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome('/Users/vetle/Downloads/chromedriver')
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        email = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')

        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)  # not necessary
        followButton = self.browser.find_element_by_css_selector('button')
        followButton.click()


bot = InstagramBot('fitnessforcoder', '12356123qWl12356')
bot.signIn()