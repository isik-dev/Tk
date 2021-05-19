from tkinter import *


def button_clicked():
    print("Entry made by the user")
    user_input = entry1.get()
    output = int(user_input) * 1.60934
    km_calculated.config(text=round(output, 1))


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Miles - Label
miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2, row=0)

# Km - Label
km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=2, row=1)

# Km - Label (after calculation)
km_calculated = Label(text="0")
km_calculated.grid(column=1, row=1)

# is equal to - Label
is_equal_to = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=20, pady=20)


# Calculate - Button
calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)

# Km - Entry
entry1 = Entry(width=10)
entry1.grid(column=1, row=0)











window.mainloop()