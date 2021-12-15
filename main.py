from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_apple():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.apple.com/')
    browser.implicitly_wait(100)


    clickAirPods = browser.find_element(By.XPATH, '//*[@id="ac-globalnav"]/div/ul[2]/li[7]/a').click()

    clickAirPodsModel = browser.find_element(By.XPATH, '//*[@id="chapternav"]/div/ul/li[1]/a/span').click()

    clickBuy = browser.find_element(By.XPATH, '//*[@id="ac-localnav"]/div/div[2]/div[2]/div[2]/div[2]/a').click()

    result = browser.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[1]/div/div[1]/div/span')

    assert result.tag_name == 'span'
    assert result.text == '$129.00'

    browser.quit()
