import tkinter as tk
import crawling as cr
from tkinter.messagebox import showerror

window=tk.Tk()
window.title('meals_helper')
window.geometry('800x800')

cnt=0

def input_btn(event=''): #입력 버튼
    global cnt
    outx.delete('1.0','end')
    try:
        ex=inx.get('1.0','end-1c')
        for i in ex.split('\n'):
            print(i)
            menu_lab.config(text=i)
            outx.insert('1.0',cr.get_recipe(cr.get_number(i,cnt)),'\n')

    except:
        showerror('Wrong','Wrong input')
        
def next_btn(): #다음 버튼 
    global cnt
    print(cnt)

    cnt+=1
    input_btn()

def priv_btn(): #이전 버튼
    global cnt
    print(cnt)
    if cnt<0:
        cnt=0
        showerror('Wrong','첫 페이지 입니다')
        return 0
    cnt-=1
    input_btn()
    

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
menu_lab=tk.Label(window,text='', font=20)
menu_lab.place(x=1,y=400)

#메뉴 입력 버튼
ip_btn=tk.Button(window, text='입력', width=10, height=3, command=input_btn)
ip_btn.place(x=5, y=280)

#다음 버튼
nx_btn=tk.Button(window,text='다음', width=10, height=3, command=next_btn,background='cyan')
nx_btn.place(x=90,y=575)

#이전 버튼
pr_btn=tk.Button(window,text='이전', width=10, height=3, command=priv_btn,background='yellow')
pr_btn.place(x=5, y=575)






window.bind('<F2>',input_btn) # 단축키, f2 == input_btn
window.mainloop()