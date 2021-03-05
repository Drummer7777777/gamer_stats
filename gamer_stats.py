from selenium import webdriver
import requests, time

link = 'https://worldoftanks.ru/ru/community/accounts/#wot&at_search='

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_nikname = browser.find_element_by_id('account_table_search')
    input_nikname.send_keys('Drummer7777777')
    time.sleep(3)
    btn = browser.find_elements_by_xpath('//div[@class="js-autocomplete b-autocomplete_item"]/div[1]')
    btn.click()

finally:
    time.sleep(5)
    browser.quit()