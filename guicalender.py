from tkinter import *
import calendar
root = Tk()
root.title("GUI Calender by @happy_coding01")
year = 2021
mycal=calendar.calendar(year)
cal_year = Label(root,text=mycal,font="Consolas 10 bold")
cal_year.pack()
root.mainloop()