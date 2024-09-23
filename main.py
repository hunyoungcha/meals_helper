import tkinter as tk
import crawling as cr
from tkinter import filedialog
from tkinter.messagebox import showerror
import make_hwp

window=tk.Tk()
window.title('meals_helper')
window.geometry('800x800')

recipe_cnt=0 #한 메뉴의 레시피 번호, ex)쌀밥의 레시피 1번 2번 ...
menu_list=[] #input text에서 입력받은 여러 줄의 메뉴를 저장하는 리스트
menu_cnt=0   #menu_list의 인덱스 번호를 컨트롤 하기 위한 변수

def input_btn(): #입력 버튼
    global menu_list, menu_cnt, recipe_cnt
    menu_cnt=0
    recipe_cnt=0
    menu_list=[]
    total_material.delete('1.0','end-1c')
    outx.delete('1.0','end-1c')
    ex=inx.get('1.0','end-1c')
    menu_list=ex.split('\n')
    search(menu_list[menu_cnt])

def search(menu):
    global recipe_cnt
    outx.delete('1.0','end')
    menu_lab.config(text=menu)
    outx.insert('1.0', ' '.join(cr.get_recipe(cr.get_number(menu, recipe_cnt))), '\n')
    outx.insert('end', ' ')




def next_btn(): #다음 버튼 
    global recipe_cnt,menu_list,menu_cnt
    recipe_cnt+=1
    search(menu_list[menu_cnt])

def priv_btn(): #이전 버튼
    global recipe_cnt,menu_list,menu_cnt
    if recipe_cnt<1:
        recipe_cnt=0
        showerror('Wrong','첫 페이지 입니다')
        return 0
    recipe_cnt-=1
    search(menu_list[menu_cnt])


def save_btn_f(): #--> 버튼
    global menu_cnt, menu_list,recipe_cnt
    oup=outx.get('1.0','end-1c')
    total_material.insert('end-1c',oup)
    outx.delete('1.0','end')
    recipe_cnt=0
    menu_cnt+=1
    try:
        search(menu_list[menu_cnt])
    except:
        return 0

def Load_meal():
    global meal_img
    meal_img = filedialog.askopenfilename(initialdir="/", title="meal_img",filetypes=(("*.jpg","*.jpg"),("*.png","*.png"),("all files", "*.*")))
    meal_lab.config(text=meal_img.split('/')[-1])

def Load_snack():
    global snack_img
    snack_img = filedialog.askopenfilename(initialdir="/", title="snack_img",filetypes=(("*.jpg","*.jpg"),("*.png","*.png"),("all files", "*.*")))
    snack_lab.config(text=snack_img.split('/')[-1]) 

def run():
    menu=inx.get('1.0','end-1c').split('\n')
    mat=total_material.get('1.0','end-1c').split(' ')
    snack=snack_text.get('1.0','end-1c').split(' ')
    file_name=name_text.get('1.0','end-1c')
    make_hwp.make_hwp(menu, mat, snack, file_name, meal_img, snack_img)
    

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
save_btn=tk.Button(window, width=12, height=4, text='-->' , background='gray',foreground='white', command=save_btn_f)
save_btn.place(x=280,y=460)

#생성 버튼
create_btn=tk.Button(window,width=22, height=4, text='생성', background='blue',foreground='white', command=run)
create_btn.place(x=5, y=640)

#급식 라벨
meal_lab=tk.Label(window,text="*업로드 된 급식 사진이 없습니다.",font=20)
meal_lab.place(x=420,y=30)
#급식 버튼
meal_button=tk.Button(window,text='급식 사진 업로드',width=50, background='gray',foreground='white', command=Load_meal)
meal_button.place(x=420,y=53)

#간식 라벨
snack_lab=tk.Label(window,text="*업로드 된 간식 사진이 없습니다.",font=20)
snack_lab.place(x=420,y=100)

#간식 버튼
snack_button=tk.Button(window,text='간식 사진 업로드',width=50, background='gray',foreground='white', command=Load_snack)
snack_button.place(x=420,y=123)

#간식 텍스트 라벨
snack_text_lab=tk.Label(window,text='간식', font=20)
snack_text_lab.place(x=420, y=170)

#간식 텍스트 박스
snack_text=tk.Text(window,width=45,height=1,font=30)
snack_text.place(x=420,y=193)

#파일 이름 라벨
name_lab=tk.Label(window,text="파일 이름",font=20)
name_lab.place(x=420, y=225)

#파일 이름 텍스트 박스
name_text=tk.Text(window,width=45,height=1,font=30)
name_text.place(x=420,y=248)

window.mainloop()