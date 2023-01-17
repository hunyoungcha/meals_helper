
#!/usr/bin/python3
#-*-coding:utf-8-*-
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup as bs

html=urlopen(f"https://www.10000recipe.com/recipe/list.html?q={parse.quote(input())}")
obj=bs(html,"html.parser")

f_list=obj.find_all(class_='common_sp_link') 

print(f_list[0])



# text_data=[]
# for i in obj.select('.se-fs-' ):
#     if i.get_text()!='\u200b':
#         text_data.append(i.get_text())
# print(text_data)
