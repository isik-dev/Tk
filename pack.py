from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Toss Payments")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 12, "bold"))
my_label.config(text="Welcome to Toss Payments Application")
my_label.pack()

# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
print(input.get())
input.pack()


window.mainloop()
