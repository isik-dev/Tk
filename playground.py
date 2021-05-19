# def add(*args):
#
#     sum_of_n = 0
#     for n in args:
#         sum_of_n += n
#     return sum_of_n
#
#
# print(add(1, 2, 3, 4, 5))

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(3, add=2, multiply=3)
#
#
# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#         self.seats = kwargs.get("seats")
#
#
# my_car = Car(make="Nissan", model="GT-R", color="black")
# print(my_car.model)
# print(my_car.make)
# print(my_car.color)
from tkinter import *
window = Tk()
window.title("Toss Payments")
window.geometry("500x300")

# Label

label = Label(text="Welcome to the Toss Payment Application",font=("Arial", 12, "bold"))
label.pack()
label.config(text="You are of the highest value")

# Button


def button_clicked():
    print("Wassup Buddy")
    label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


window.mainloop()
