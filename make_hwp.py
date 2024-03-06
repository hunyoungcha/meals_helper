import shutil
import win32com.client as win32

from PIL import Image

def copy_hwp(name):
    shutil.copyfile(r'./급식일지.hwp',rf'./{name[:-1]}.hwp') #한글 파일 카피 하는 코드

def open_hwp(name):
    global hwp
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
    hwp.Open(rf'C:\Users\차훈영\Desktop\python\meals_helper\{name[:-1]}.hwp') #사용 환경에 따라 경로 변경 필수

def insert_img(row,column):
    hwp.MovePos(row, column)
    hwp.PutFieldText("CellText", 1)

def img_setting(img,meal_or_snack):
    image=Image.open(img)

    if meal_or_snack=="meal":
        image.thumbnail((300,200))
        image.save(img)
    elif meal_or_snack=="snack":
        image.thumbnail((240,130))
        image.save(img)


def make_hwp(menu, mat, snack, file_name, meal_img, snack_img):
    copy_hwp(file_name)
    open_hwp(file_name)
    
    hwp.PutFieldText('m',file_name[2:4])
    hwp.PutFieldText('d',file_name[4:6])
    hwp.PutFieldText('a',file_name[6])

    hwp.PutFieldText('menu','\r\n'.join(menu))
    hwp.PutFieldText('mat',','.join(mat))
    hwp.PutFieldText('snack',','.join(snack))

    img_setting(meal_img,"meal")
    hwp.MoveToField('meal_img')
    hwp.InsertPicture(meal_img)

    img_setting(snack_img,'snack')
    hwp.MoveToField('snack_img')
    hwp.InsertPicture(snack_img)

    hwp.Save()
    hwp.Quit()

