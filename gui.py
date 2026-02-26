from tkinter import *

# root = Tk()
#
# def click():
#     yow = "Hello", entry.get()
#     label = Label(root, text=yow)
#     label.pack()
#
# entry = Entry(root)
# entry.pack()
# entry.insert(0,"Enter your name: ")
#
# # Label1 = Label(root, text="Enter your account details:")
# # Label2 = Label(root, text="WOw")
# button = Button(root, text="Click here", padx=50, command=click)
# button.pack()
# #
# # Label1.grid(row=0, column=0)
# # Label2.grid(row=1, column=0)
#
# root.mainloop()

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    entry.delete(0, END)
    entry.insert(0, number)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
add_button = Button(root, text="+", padx=40, pady=20, command=lambda: button_click)
equal_button = Button(root, text="=", padx=88, pady=20, command=lambda: button_click)
clear_button = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_click)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
add_button.grid(row=5, column=0)
equal_button.grid(row=4, column=1, columnspan=2)
clear_button.grid(row=5, column=1, columnspan=2)

root.mainloop()




