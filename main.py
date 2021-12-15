from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_apple():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.apple.com/')
    browser.implicitly_wait(100)
