# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
# root.geometry("400x400")

# Add Calendar
# cal = Calendar(root, selectmode='day',
#                year=2020, month=5,
#                day=22)

# cal.pack(pady=20)

#
# def grad_date():
#     date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
# Button(root, text="Get Date",
#        command=grad_date).pack(pady=20)
Label(root, text="name").grid(row=0)
input = Entry(root)
input.grid(row=0, column=1)

Label(root, text="text:").grid(row=1, column=0)
label = Label(root, text="")
label.grid(row=1, column=1)
# date = Label(root, text="")
# date.pack(pady=20)
def show():
    text = input.get()
    label.config(text=text)
Button(root, text="Show",
       command=show).grid(row=2)

# Execute Tkinter
root.mainloop()
