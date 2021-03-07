from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests, time

link = 'https://worldoftanks.ru/ru/community/accounts/#wot&at_search='

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    input_nikname = browser.find_element_by_id('account_table_search')
    input_nikname.send_keys('Drummer7777777')
    time.sleep(3)
    #btn = browser.find_elements_by_xpath('//div[@class="js-autocomplete b-autocomplete_item"]/div[1]')
    btn = browser.find_element_by_css_selector('[title="Поиск"]')
    #ac(browser).move_to_element(btn)
    btn.click()
    #select_gamer = WebDriverWait(browser,10).until(ec.presence_of_element_located('[href="/ru/community/accounts/7836047-Drummer7777777/"]'))
    #time.sleep(3)
    select_gamer = browser.find_element_by_css_selector('[href="/ru/community/accounts/7836047-Drummer7777777/"]')
    select_gamer.click()

finally:
    time.sleep(5)
    browser.quit()