from tkinter import *

win = Tk()
win.title("Search Time!!!")
win.geometry('550x400')

empty = Label(win, text="", font='50')
empty.pack()

l = Label(win, text='Where\'d ya wanna search?', font=('Comic Sans MS',15))
l.pack()
l2 = Label(win, text='(AKA Which Search Engine Do You Wish To Use)', font=('Comic Sans MS',15))
l2.pack()
l3 = Label(win, text="Enter 'Chrome' or 'Bing'", font=('Comic Sans MS',11,"underline","italic"))
l3.pack()

empty = Label(win, text="", font='50')
empty.pack()

Entre = Entry(win)
Entre.pack()
    
empty = Label(win, text="", font='50')
empty.pack()

def Wat_Entre():
    if Entre.get() == "Chrome":
        import Automate_Google_Search_Using_Selenium
    elif Entre.get() == "Bing":
        import Automate_Bing_Search_Using_Selenium
    else:
        empty = Label(win, text="", font='20')
        empty.pack()
        Label(win, text="Invalid Entry: Enter 'Chrome' or 'Bing'").pack()

bt = Button(win, text="Enter", command=Wat_Entre)
bt.pack()

win.mainloop()
