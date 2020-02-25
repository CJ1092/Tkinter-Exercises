from tkinter import * #importing the Tkinter package
from functools import partial

def addition(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return

def subtraction(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="Result is %d" % result)
    return

def multiplication(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result is %d" % result)
    return

def division(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)/int(num2)
    label_result.config(text="Result is %d" % result)
    return

root = Tk()
root.geometry('400x200+100+200')
root.title('Simple Calculator')

number1 = StringVar()
number2 = StringVar()

Label(root, text="Simple Calculator").grid(row=0, column=2)
Label(root, text="Enter a number").grid(row=1, column=0)
Label(root, text="Enter another number").grid(row=2, column=0)
labelResult = Label(root)
labelResult.grid(row=7, column=2)

Entry(root, textvariable=number1).grid(row=1, column=2)
Entry(root, textvariable=number2).grid(row=2, column=2)

addition = partial(addition, labelResult, number1, number2)
subtraction = partial(subtraction, labelResult, number1, number2)
multiplication = partial(multiplication, labelResult, number1, number2)
division = partial(division, labelResult, number1, number2)

Button(root, text="Add", command=addition).grid(row=3, column=0)
Button(root, text="Subtract", command=subtraction).grid(row=3, column=1)
Button(root, text="Multiply", command=multiplication).grid(row=3, column=2)
Button(root, text="Divide", command=division).grid(row=3, column=3)

root.mainloop()
