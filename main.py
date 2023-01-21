import tkinter as tk
import crawling as cr


window=tk.Tk()
window.title('meals_helper')
window.geometry('800x800')

def btn_click():
    outx.delete('1.0','end')
    try:
        outx.insert('1.0',cr.get_recipe(cr.get_number(inx.get())))
    except:
        #enctry위에 라벨 하나 만들건데 그 위에 잘못 입력되었다고 표시 하기

inx=tk.Entry(window, width=100)
btn=tk.Button(window, text='입력', width=10, height=3, command=btn_click)
outx=tk.Text(window, width=40, height=10, font=10)




inx.pack()
btn.pack()
outx.pack(side='left')
window.mainloop()