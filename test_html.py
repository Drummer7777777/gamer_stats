#составление html страницы
def insert_in_html(nikname,list_tanks): 
    #запись в список строк из исходника html   
    with open('statss.html','r', encoding='utf-8') as f:
        allf = f.readlines()
    #константа для вставки 6ая строка для таблицы
    j=6
    #вставка ника в список с исходником html
    allf.insert(3,nikname)
    #вставка таблицы в список html исходника
    for i in range(len(list_tanks)):
        allf.insert(j, list_tanks[i])
        j+=1
    #создание итоговой html из готового списка
    with open(f'{nikname}.html','w+', encoding='utf-8') as f:
        for i in range(len(allf)):
            f.write(allf[i])