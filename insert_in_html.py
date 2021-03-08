def insert_data(naz,vih_type,level,tank,count_battle,percent_win,rank,mark):
    with open('statss.txt','a+') as f:
        #f.write('<tr><th>Страна</th><th>Тип техники</th><th>Уровень</th><th>Танк</th><th>Количество боев</th><th>Процент побед</th><th>Знак классности</th><th>Отметки на стволе</th></tr>') 
        #f.seek(-1)
        lines = f.readlines()
        print(lines)
        count_lines = len(lines)
        print(count_lines)
        #for line in lines:
        #    f.readline()
        line = (f'<tr><td>{naz}</td><td>{vih_type}</td><td>{level}</td><td>{tank}</td><td>{count_battle}</td><td>{percent_win}</td><td>{rank}</td><td>{mark}</td></tr>')
        if count_lines > 0:
            lines += ['\n'] + [line]
        else:
            lines = [line]
        for line in lines:
            f.write(line)