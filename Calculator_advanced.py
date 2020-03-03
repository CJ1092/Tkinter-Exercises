# calculator using Tkinter

from tkinter import *

value = "" # variable declared globally to store value


# Function to update value
def press(num):
	global value

	value = value + str(num)

	display.set(value) # update the value by using set method


# Function to evaluate the final value
def equal():
	try:

		global value

		total = str(eval(value)) # converting to string for display
        
		display.set(total)

		value = ""

	except:

		display.set(" error ")
		value = ""


# Function to clear the contents
def clear():
	global value
	value = ""
	display.set("")

screen = Tk()
screen.configure(background="light blue")
screen.title("Calculator")
screen.geometry("265x125")

display = StringVar()

Entry(screen, textvariable=display).grid(columnspan=4, ipadx=70)

display.set('')

Button(screen, text=' 1 ', command=lambda: press(1), height=1, width=7).grid(row=2, column=0)
Button(screen, text=' 2 ', command=lambda: press(2), height=1, width=7).grid(row=2, column=1)
Button(screen, text=' 3 ', command=lambda: press(3), height=1, width=7).grid(row=2, column=2)
Button(screen, text=' 4 ', command=lambda: press(4), height=1, width=7).grid(row=3, column=0)
Button(screen, text=' 5 ', command=lambda: press(5), height=1, width=7).grid(row=3, column=1)
Button(screen, text=' 6 ', command=lambda: press(6), height=1, width=7).grid(row=3, column=2)
Button(screen, text=' 7 ', command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
Button(screen, text=' 8 ', command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
Button(screen, text=' 9 ', command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
Button(screen, text=' 0 ', command=lambda: press(0), height=1, width=7).grid(row=5, column=0)

Button(screen, text=' + ', command=lambda: press("+"), height=1, width=7).grid(row=2, column=3)
Button(screen, text=' - ', command=lambda: press("-"), height=1, width=7).grid(row=3, column=3)
Button(screen, text=' * ', command=lambda: press("*"), height=1, width=7).grid(row=4, column=3)
Button(screen, text=' / ', command=lambda: press("/"), height=1, width=7).grid(row=5, column=3)
Button(screen, text=' = ', command=equal, height=1, width=7).grid(row=5, column=2)

Button(screen, text='Clear', command=clear, height=1, width=7).grid(row=5, column=1)

screen.mainloop()
