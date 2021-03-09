def insert_in_html(nikname):    
    with open('statss.html','r', encoding='utf-8') as f:
        allf = f.readlines()
        print(allf)
        with open(f'{nikname}.txt','r') as ff:
            allff = ff.readlines()
            print(allff)
            print(len(allff))
    j=5
    for i in range(len(allff)):
        allf.insert(j, allff[i])
        j+=1
    with open(f'{nikname}.html','w+', encoding='utf-8') as f:
        #for i in range(len(allff)-1):
        #    allf.insert(j, allff[i])
        #    j+=1
        for i in range(len(allf)):
            f.write(allf[i])
            #print(allf)