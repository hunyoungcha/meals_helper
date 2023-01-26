#클래스화 시키기
#https://engineer-mole.tistory.com/190


import tkinter as tk
import crawling as cr
from tkinter import filedialog
from tkinter.messagebox import showerror

window=tk.Tk()
window.title('meals_helper')
window.geometry('800x800')

recipe_cnt=0


def input_btn(): #입력 버튼
    global menu_list, menu_cnt
    menu_cnt=0
    total_material.delete('1.0','end-1c')
    ex=inx.get('1.0','end-1c')
    menu_list=ex.split('\n')
    print("menu_list= ",menu_list)
    search(menu_list[menu_cnt])

def search(menu):
    global recipe_cnt
    outx.delete('1.0','end')
    try:
        menu_lab.config(text=menu)
        outx.insert('1.0',cr.get_recipe(cr.get_number(menu,recipe_cnt)),'\n')
    except:
        showerror('Wrong','Wrong input')   


def next_btn(): #다음 버튼 
    global recipe_cnt,menu_list,menu_cnt
    recipe_cnt+=1
    print("recipe_cnt= ",recipe_cnt)
    search(menu_list[menu_cnt])

def priv_btn(): #이전 버튼
    global recipe_cnt,menu_list,menu_cnt
    print(recipe_cnt)
    if recipe_cnt<1:
        recipe_cnt=0
        showerror('Wrong','첫 페이지 입니다')
        return 0
    recipe_cnt-=1
    print("recipe_cnt= ",recipe_cnt)
    search(menu_list[menu_cnt])


def save_btn(): #--> 버튼
    global menu_cnt, menu_list
    oup=outx.get('1.0','end-1c')
    print('oup= ',oup)
    total_material.insert('end-1c',oup)
    outx.delete('1.0','end')
    menu_cnt+=1
    try:
        search(menu_list[menu_cnt])
    except:
        return 0


def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("*.jpg","*.png"),
                                          ("all files", "*.*")))   
    return filename




    

#메뉴 입력 위 라벨
lab=tk.Label(window, text='메뉴를 입력하세요.', font=20)
lab.place(x=1,y=1)

#메뉴 입력 텍스트 박스
inx=tk.Text(window, width=50, height=15, font=30)
inx.place(x=1,y=30)

#재료 아웃풋 텍스트 박스
outx=tk.Text(window, width=30, height=8, font=20)
outx.place(x=1,y=430)

#메뉴 제목 아웃풋 라벨
menu_lab=tk.Label(window,text='메뉴 이름', font=20)
menu_lab.place(x=1,y=400)

#메뉴 입력 버튼
ip_btn=tk.Button(window, text='입력', width=10, height=3, command=input_btn,background='gray', foreground='white')
ip_btn.place(x=5, y=280)

#다음 버튼
nx_btn=tk.Button(window,text='다음', width=10, height=3, command=next_btn,background='gray', foreground='white')
nx_btn.place(x=90,y=575)

#이전 버튼
pr_btn=tk.Button(window,text='이전', width=10, height=3, command=priv_btn,background='gray',foreground='white')
pr_btn.place(x=5, y=575)

#총 재료 라벨
total_lab=tk.Label(window,text='전체 재료', font=20)
total_lab.place(x=405, y=400)

#총 재료 텍스트 박스
total_material=tk.Text(window, width=48,height=20,font=30)
total_material.place(x=400, y=430)

#--> 버튼
save_btn=tk.Button(window, width=12, height=4, text='-->' , background='gray',foreground='white', command=save_btn)
save_btn.place(x=280,y=460)

#생성 버튼
create_btn=tk.Button(window,width=22, height=4, text='생성', background='blue',foreground='white')
create_btn.place(x=5, y=640)

#급식 라벨
meal_lab=tk.Label(window,text="*업로드 된 급식 사진이 없습니다.",font=20)
meal_lab.place(x=420,y=30)
#급식 버튼
meal_button=tk.Button(window,text='급식 사진 업로드',width=50, background='gray',foreground='white', command=Load)
meal_button.place(x=420,y=53)

#간식 라벨
snack_lab=tk.Label(window,text="*업로드 된 간식 사진이 없습니다.",font=20)
snack_lab.place(x=420,y=100)

#간식 버튼
snack_button=tk.Button(window,text='간식 사진 업로드',width=50, background='gray',foreground='white')
snack_button.place(x=420,y=123)

# window.bind('<F2>',input_btn) # 단축키, f2 == input_btn
window.mainloop()