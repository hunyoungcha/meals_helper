import shutil
import win32com.client as win32

#https://www.codingnow.co.kr/python/?bmode=view&idx=6494279&back_url=&t=board&page= <-- 한글 자동화 참고 하면 좋을 블로그 #보안 팝업 7:05 부터
#https://www.hancom.com/board/devmanualList.do?artcl_seq=3934 <-- 한글 개발 문서



hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")



def make_hwp(name):
    shutil.copyfile(r'./급식일지.hwp',rf'./{name}.hwp') #카피 하는 코드
    hwp.Open(rf'C:\Users\차훈영\Desktop\python\meals_helper/{name}.hwp')
    field_list=[i for i in hwp.GetFieldList().split('\x02')] #각각의 필드가 저장되있는 리스트
    print(field_list)
make_hwp('2037010')