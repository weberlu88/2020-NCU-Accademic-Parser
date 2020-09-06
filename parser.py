from bs4 import BeautifulSoup

# 讀成績
path = '成績查詢的HTML/成績查詢.html'
with open(path, 'r', encoding="utf-8") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.select('tbody')[0]
title = table.select('tr', {"class":"list"})[0]
courses = table.find_all('tr', {"class":"list1"})

# program_course = {}
# managem_course = {}
# for course in courses:
    
#     content = course.select('td')
#     _id = content[2].text.split()[0]
#     name = ''.join(content[2].text.split(' ')[1:])
#     score = content[-1].text
    
#     print(_id, name, score)

# 輸出成csv
path = '所有課程.csv'
with open(path, 'w', encoding="utf-8") as file:
    
    file.writelines(['課號','課名','成績'])
    for course in courses:
        content = course.select('td')
        _id   = content[2].text.split()[0]
        name  = ''.join(content[2].text.split(' ')[1:])
        score = content[-1].text

        line = "{},{},{}\n".format(_id, name, int(score))
        file.writelines(line)