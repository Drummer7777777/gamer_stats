from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import requests, time
from insert_in_htmll import insert_data
from test_html import insert_in_html

link = 'https://worldoftanks.ru/ru/community/accounts/#wot&at_search='

nacional = {
    'us':'США',
    'franc':'ФРАНЦИЯ',
    'uss':'СССР',
    'german':'ГЕРМАНИЯ',
    'u':'ВЕЛИКОБРИТАНИЯ',
    'swede':'ШВЕЦИЯ',
    'czec':'ЧЕХИЯ',
    'japa':'ЯПОНИЯ',
    'ital':'ИТАЛИЯ',
    'polan':'ПОЛЬША',
    'chin':'КИТАЙ'
}

def vihicle_typs(a):
    if 'heavytank' in a:
        return 'Тяжелый танк'
    elif 'mediumtank' in a:
        return 'Средний танк'
    elif 'lighttank' in a:
        return 'Легкий танк'
    elif 'at-spg' in a:
        return 'ПТ-САУ'
    elif 'spg' in a:
        return 'САУ'
    
def ranks(a):
    if 'master' in a:
        return 'Мастер'
    elif '01' in a:
        return '1 степень'
    elif '02' in a:
        return '2 степень'
    elif '03' in a:
        return '3 степень'
    else:
        return 'Нет классности'

def marks(a):
    if '1_mark' in a:
        return '1 отметка'
    elif '2_marks' in a:
        return '2 отметки'
    elif '3_marks' in a:
        return '3 отметки'


try:
    nikname = 'ALEX00000000000000000'
    tank_in_table = 2
    list_tanks = []
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    input_nikname = browser.find_element_by_id('account_table_search')
    input_nikname.send_keys(nikname)
    #time.sleep(3)
    #btn = browser.find_elements_by_xpath('//div[@class="js-autocomplete b-autocomplete_item"]/div[1]')
    btn = browser.find_element_by_css_selector('[title="Поиск"]')
    #ac(browser).move_to_element(btn)
    btn.click()
    #select_gamer = WebDriverWait(browser,10).until(ec.presence_of_element_located('[href="/ru/community/accounts/7836047-Drummer7777777/"]'))
    #time.sleep(3)
    try:
        select_gamer = browser.find_element_by_css_selector('.t-table> tbody> tr:nth-child(1)> td> a')
        select_gamer.click()
    except NoSuchElementException:
        print('Игрока с таким именем нет')
    else:
        #парсинг таблицы танков
        link_more = browser.find_element_by_class_name('link-more__no-arrow')
        attr_link_more = link_more.get_attribute('style')
        if attr_link_more == 'display: none;':
            pass
        else:
            ac(browser).click(link_more).perform()
        #table_tanks = browser.find_element_by_css_selector('[.table_inner> item:nth-child(2)> .table_row> item:nth-child(2)> span]')
        table_tanks = browser.find_element_by_css_selector('.table_inner')
        while True:
            try:
                row_tank = table_tanks.find_element_by_css_selector(f'div:nth-child({tank_in_table})> .table_row')
            except NoSuchElementException:
                break
            else:
                #нация
                flag = row_tank.find_element_by_css_selector(f'div:nth-child(2)> span')
                naz = nacional.get(flag.get_attribute('class')[27:-1:1])
                #тип
                vihicle_type = row_tank.find_element_by_css_selector('div:nth-child(3)> span').get_attribute('class')
                vih_type = vihicle_typs(vihicle_type)
                #уровень
                level = row_tank.find_element_by_css_selector('div:nth-child(4)').text
                #танк
                tank = row_tank.find_element_by_css_selector('div:nth-child(5)> span').text
                #количество боев
                count_battle = row_tank.find_element_by_css_selector('div:nth-child(6)> span').text
                #процент побед
                percent_win = row_tank.find_element_by_css_selector('div:nth-child(7)> span').text
                #знак классности
                try:
                    rank = ranks(row_tank.find_element_by_css_selector('div:nth-child(8)> span').get_attribute('class'))
                except NoSuchElementException:
                    rank = 'Нет классности'
                #отметки на орудии
                try:
                    mark = marks(row_tank.find_element_by_css_selector('div:nth-child(9)> img').get_attribute('src'))
                except NoSuchElementException:
                    mark = 'Нет отметок'



                print(naz, vih_type, level,tank,count_battle,percent_win,rank,mark)
                insert_data(nikname,naz, vih_type, level,tank,count_battle,percent_win,rank,mark)
                tank_in_table+=1
finally:
    insert_in_html(nikname)
    time.sleep(5)
    browser.quit()