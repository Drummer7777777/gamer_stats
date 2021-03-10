#добавление строки с танком в список
def add_list_tanks(list_tanks,nikname,naz,vih_type,level,tank,count_battle,percent_win,rank,mark):
    line = f'<tr><td>{naz}</td><td>{vih_type}</td><td>{level}</td><td>{tank}</td><td>{count_battle}</td><td>{percent_win}</td><td>{rank}</td><td>{mark}</td></tr>\n'
    list_tanks.append(line)