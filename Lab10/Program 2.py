import tkinter
window = tkinter.Tk()
window.title("Two Frames with Widgets")
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")
btn1 = tkinter.Button(top_frame,text = "Button1",fg = "red").pack()#
btn2 = tkinter.Button(top_frame,text = "Button2",fg = "green").pack()#
btn3 = tkinter.Button(bottom_frame,text = "Button2",fg = "purple").pack(side = "left")
btn4 = tkinter.Button(bottom_frame,text = "Button2",fg = "orange").pack(side = "right")
window.mainloop()