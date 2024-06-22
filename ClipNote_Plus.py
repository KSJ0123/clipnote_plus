import tkinter
import clipboard
import threading

window = tkinter.Tk()
window.title('Notes Plus')
window.geometry('400x500+100+100')

#쓰레드 생성
def th():
    th = threading.Thread(target=clipture)
    th.daemon = True
    th.start()

#화면 고정
def pined():
    if cv1.get()==1:
        window.wm_attributes("-topmost",1)
    else:
        window.wm_attributes("-topmost",0)

#클립보드 연동
def clipture():
    result2=""
    while True:
        result=clipboard.paste()
        if result != result2 :
            result2=result
            clippaste=tkinter.Text(window,width=50,height=10,)
            clippaste.pack()
            clippaste.insert('1.0',result2)
            clipdelet=tkinter.Button(window,text='X')
            clipdelet.pack()
            clipdelet.config(command=lambda cl=clippaste , dl=clipdelet : clip_delet(cl,dl))
        if cv2.get() != 1 :
            break
#삭제
def clip_delet(cl,dl):
    dl.destroy()
    cl.destroy()
    

#메모 추가
def add_meom1():
    meom=tkinter.Text(window,width=50,height=10)
    meom.pack()
    delet=tkinter.Button(window,text='X',command=lambda: (meom.destroy(),delet.destroy()))
    delet.pack()

#pin 체크박스
cv1=tkinter.IntVar()
pin=tkinter.Checkbutton(window,text="고정",variable=cv1,command=pined)
pin.pack()

#클립보드 체크박스
cv2=tkinter.IntVar()
clip=tkinter.Checkbutton(window,text="클립보드 연동",variable=cv2,command=th)
clip.pack()

#메모추가 버튼
add_memo=tkinter.Button(window,text='+',width=30,command=add_meom1)
add_memo.pack()



window.mainloop()
