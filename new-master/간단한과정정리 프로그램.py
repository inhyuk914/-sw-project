import tkinter
import os
print (os.path.dirname(os.path.realpath("C:\\Users\\inhyu\\OneDrive\\사진")) )
num=0
def forward_image():
    global num
    num=num-1
    label_Img.configure(image=py_Img[num])

def next_image():
    global num
    num=num+1
    label_Img.configure(image=py_Img[num])

win=tkinter.Tk()
win.title("블록체인 과정 표시.")
# Win Size Control
win.geometry('1000x1000')
win.resizable(width=1, height=0)
py_Img=[tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인1.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인2.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인3.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인4.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인5.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인6.png"),
        tkinter.PhotoImage(file="C:\\Users\\inhyu\\OneDrive\\사진\\블록체인7.png")]
label_Img=tkinter.Label(win,image=py_Img[0])
label_Img.pack()

button=tkinter.Button(win,text="이전", command=forward_image)
button.pack()

button=tkinter.Button(win,text="다음", command=next_image)
button.pack()

win.mainloop()
