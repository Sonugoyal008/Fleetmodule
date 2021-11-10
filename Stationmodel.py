Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> window = Tk()
>>> window.title("Station Model")
''
>>> window.geometry('400x400')
''
>>> window.configure(background = "grey");
>>> a = Label(window ,text = "Station Name").grid(row = 0,column = 0)
>>> b = Label(window ,text = "Station code").grid(row = 1,column = 0)
>>> c = Label(window ,text = "Latitude").grid(row =2 ,column = 0)
>>> d = Label(window ,text = "Longitude").grid(row = 3,column = 0)
>>> e = Label(window ,text = "city").grid(row = 4,column = 0)
>>> a1 = Entry(window).grid(row = 0,column = 1)
>>> b1 = Entry(window).grid(row = 1,column = 1)
>>> c1 = Entry(window).grid(row = 2,column = 1)
>>> d1 = Entry(window).grid(row = 3,column = 1)
>>> e1 = Entry(window).grid(row = 4,column = 1)
>>> def clicked():
	res="Welcome to" +txt.get()
	lbl.configure(text =res)
    btn=ttk.Button(window,text="submit").grid(row=5,coloumn=0)
    
SyntaxError: unindent does not match any outer indentation level
>>> def clicked():
	 res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()
SyntaxError: unindent does not match any outer indentation level
>>> def clicked():
	res = "Welcome to " + txt.get()
	lbl.configure(text= res)
	btn = ttk.Button(window ,text="Submit").grid(row=5,column=0)
	window.mainloop()

>>> 
