from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.common.exceptions import NoSuchElementException
import requests
from test_html import insert_in_html
from list_stats import add_list_tanks

link = 'https://worldoftanks.ru/ru/community/accounts/#wot&at_search='

#страны
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

#типы техники
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

#классность    
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

#отметки
def marks(a):
    if '1_mark' in a:
        return '1 отметка'
    elif '2_marks' in a:
        return '2 отметки'
    elif '3_marks' in a:
        return '3 отметки'


try:
    nikname = input()
    #счетчик для парсинга из таблицы, танки начинаются с 2
    tank_in_table = 2
    #список куда парсятся данные
    list_tanks = []
    browser = webdriver.Chrome()
    #ожидание появление элементов
    browser.implicitly_wait(5)
    browser.get(link)
    #поиск игрока
    input_nikname = browser.find_element_by_id('account_table_search')
    input_nikname.send_keys(nikname)
    btn = browser.find_element_by_css_selector('[title="Поиск"]')
    btn.click()
    try:
        select_gamer = browser.find_element_by_css_selector('.t-table> tbody> tr:nth-child(1)> td> a')
        select_gamer.click()
    except NoSuchElementException:
        print('Игрока с таким именем нет')#если нет такого игрока
    else:
        #парсинг таблицы танков
        #поиск кнопки Показать больше техники, чтобы открыть таблицу полностью
        link_more = browser.find_element_by_class_name('link-more__no-arrow')
        attr_link_more = link_more.get_attribute('style')
        if attr_link_more == 'display: none;':
            pass#если кнопки нет
        else:
            ac(browser).click(link_more).perform()#нажимаем если есть
        #table_tanks = browser.find_element_by_css_selector('[.table_inner> item:nth-child(2)> .table_row> item:nth-child(2)> span]')
        #таблица с танками на странице
        table_tanks = browser.find_element_by_css_selector('.table_inner')
        #цикл прохождения по строкам
        while True:
            try:
                #находит строку с танком
                row_tank = table_tanks.find_element_by_css_selector(f'div:nth-child({tank_in_table})> .table_row')
            except NoSuchElementException:
                #если нет строки с таким индексом(начинали с 2) выход из цикла
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
                    #если есть
                    rank = ranks(row_tank.find_element_by_css_selector('div:nth-child(8)> span').get_attribute('class'))
                except NoSuchElementException:
                    rank = 'Нет классности'
                #отметки на орудии
                try:
                    #если есть
                    mark = marks(row_tank.find_element_by_css_selector('div:nth-child(9)> img').get_attribute('src'))
                except NoSuchElementException:
                    mark = 'Нет отметок'
                #вывод записанной строки
                print(naz, vih_type, level,tank,count_battle,percent_win,rank,mark)
                #добавление строки с html тегами в список list_tanks
                add_list_tanks(list_tanks,nikname,naz, vih_type, level,tank,count_battle,percent_win,rank,mark)
                #увеличение счетчика для перехода на следующую строку
                tank_in_table+=1
finally:
    insert_in_html(nikname, list_tanks)#сборка итоговой html из списка list_tanks
    browser.quit()