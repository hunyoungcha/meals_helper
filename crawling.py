#!/usr/bin/python3
#-*-coding:utf-8-*-
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint

def get_number(menu_name, num):  #메뉴 이름을 입력 받으면 레시피 넘버를 넘겨줌
    html=urlopen(f"https://www.10000recipe.com/recipe/list.html?q={parse.quote(menu_name)}")
    obj=bs(html,"html.parser")

    f_list=list(map(str,obj.find_all(class_='common_sp_link')))
    pag_num=re.sub(r'[^0-9]','', f_list[num].split('\n')[0])  #레시피 넘버가 저장됨
    return pag_num

def get_recipe(pag_num): #음식의 재료를 리턴하는 함수
    html=urlopen(f"https://www.10000recipe.com/recipe/{parse.quote(pag_num)}")
    obj=bs(html,"html.parser")

    matArea=obj.find('div',{'id':'divConfirmedMaterialArea'})
    matAreaDiv = matArea.find_all('div', {'class' : 'ingre_list_name'})
    
    result =[]

    for div in matAreaDiv:
        [span.extract() for span in div.find_all('span')]
        text = div.get_text(strip=True)
        result.append(text)

    return result
