import tkinter
window = tkinter.Tk()
window.title("Login Page")

tkinter.Label(window, text = "UserName").grid(row = 0)
tkinter.Entry(window).grid(row = 0 , column = 1)
tkinter.Label(window , text = "Password").grid(row = 1)
tkinter.Entry(window).grid(row = 1 ,column = 1)

tkinter.Checkbutton(window , text = "Keep me logged In").grid(columnspan = 2)
window.mainloop()