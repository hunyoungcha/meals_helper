
#!/usr/bin/python3
#-*-coding:utf-8-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen(f"https://www.10000recipe.com/recipe/list.html?q={input().encode('utf-8')}")
obj=bs(html,"html.parser")

print(obj)
# for link in obj.find_all('a',class_="common_sp_link"):
#     print(link.text.strip(), link.get('href'))

# text_data=[]
# for i in obj.select('.se-fs-' ):
#     if i.get_text()!='\u200b':
#         text_data.append(i.get_text())
# print(text_data)
