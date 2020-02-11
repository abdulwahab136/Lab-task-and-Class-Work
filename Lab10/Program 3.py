import tkinter
window = tkinter.Tk()
window.title("Playing with GUI")
tkinter.Label(window, text = "Sufficent Width",fg = "white", bg = "purple").pack()

tkinter.Label(window,text = "Taking All available width of X",fg = "white", bg = "green").pack(fill = "x")
tkinter.Label(window,text = "Taking All available Height of Y",fg = "white", bg = "black").pack(side = "left",fill = "y")
window.mainloop()