from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=3, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=4, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=2)

result_label = Label(text="0")
result_label.grid(column=3, row=2)
KM_Label = Label(text="KM")
KM_Label.grid(column=4, row=2)



def miles_to_km():
    miles = float(miles_entry.get())
    km_result = round(miles * 1.609)
    result_label.config(text=f"{km_result}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=3, row=3)

window.mainloop()