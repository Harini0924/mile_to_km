from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width =200, height=100)
window.config(padx=20,pady=20)


#label
my_label1 = Label(text="is equal to")
my_label1.grid(column=1,row=1)

#label
zero_label = Label(text=0)
zero_label.grid(column=2,row=1)


#Button
def button_clicked():
    miles=float(input.get())
    km= round(miles*1.609)
    zero_label.config(text=km)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2,row=2)

#Entry
input = Entry(width=10)
input.grid(column=2,row=0)



#labels

my_label2= Label(text="Miles")
my_label2 .grid(column=3,row=0)

my_label2= Label(text="Km")
my_label2 .grid(column=3,row=1)

window.mainloop()