from tkinter import *

root = Tk()
e = Entry(root, width=50)
# e = Entry(root, width=50, fg='blue', bg='white')
# e = Entry(root, width=50, borderwidth=2)
e.pack()
e.insert(0, 'Enter Your Name: ')

def myClick():
    if e.get() != '':
        hello = 'Hello ' + e.get()
        myLabel = Label(root, text=hello)
        myLabel.pack()

myButton = Button(root, text='Enter Your Name', command=myClick)
myButton.pack()

root.mainloop()