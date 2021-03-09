def insert_data(nikname,naz,vih_type,level,tank,count_battle,percent_win,rank,mark):

    line = f'<tr><td>{naz}</td><td>{vih_type}</td><td>{level}</td><td>{tank}</td><td>{count_battle}</td><td>{percent_win}</td><td>{rank}</td><td>{mark}</td></tr>\n'
    with open(f'{nikname}.txt', 'a+') as fl:#, encoding='utf-8') as fl:
        fl.writelines(line)
