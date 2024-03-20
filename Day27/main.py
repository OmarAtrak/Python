from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=70, pady=20)


text_input = Entry(width=10)
text_input.insert(END, "0")
text_input.grid(column=1, row=0)


miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)


is_equal_text = Label(text="is equal to")
is_equal_text.grid(column=0, row=1)


km_value_text = Label(text="0")
km_value_text.grid(column=1, row=1)


km_text = Label(text="Km")
km_text.grid(column=2, row=1)


def calculate():
    miles = float(text_input.get())
    km = round(miles * 1.609)
    km_value_text.config(text=f'{km}')


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
