global Entry_1

from tkinter import *
window = Tk()
window.title("Water reminder")
window.geometry("400x400")
window.configure(bg = "lightblue")

label_1 = Label(text= "Hi, Please enter you name.")
label_1.configure(bg="lightblue", foreground="blue", font=('Times', 13))
label_1.place(x = 120, y = 200)

Entry_1 = Entry()
Entry_1.place(x = 145, y = 230)

def new_window():
        window.destroy()
        top = Tk()
        top.configure(bg = "lightblue")
        top.title("Water reminder - Home")
        top.geometry("400x400")
        Entry1 = Entry_1.get()
        lab = Label(top, text="Hey," + Entry1)
        lab.configure(bg="lightblue", font=('Times'))
        lab.place(x=20, y = 30)

        lab_2 = Label(top, text="Please enter Your weight")
        lab_2.configure(bg="lightblue", font=('Calibri'))
        lab_2.place(x=120, y = 100)

        Entry_2 = Entry()
        Entry_2.place(x = 140, y = 130)

        button_2 = Button(text="Submit")
        button_2.configure(bg="sky Blue", foreground="black")
        button_2.place(x = 175, y = 180)

        weight = Entry_2.get()
        print(weight)
        water_to_be_consumed = 35 * weight
        in_liters = water_to_be_consumed/1000
        print(in_liters)

        lab_3 = Label(top, text="You should drink " + in_liters + "Litres Everyday") 
        lab_2.configure(bg="lightblue", font=('Calibri'))
        lab_2.place(x=120, y = 210)

        top.mainloop()

button_1 = Button(text="START", command = new_window)
button_1.configure(bg="sky Blue", foreground="black")
button_1.place(x = 180, y = 260)

window.mainloop()
