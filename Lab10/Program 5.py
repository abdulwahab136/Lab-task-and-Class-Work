import tkinter
window = tkinter.Tk()
window.title("Binding Functions")

def say_Assalam():
    tkinter.Label(window, text = "Assalam o Alaikum").pack()

tkinter.Button(window,text = "Click Me!!!",command = say_Assalam()).pack()
window.mainloop()