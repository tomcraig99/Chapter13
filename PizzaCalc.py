from msilib.schema import Class
import tkinter
import tkinter.messagebox
from turtle import left


class PizzaCalc:

    def __init__(self):
        #creating window
        self.main = tkinter.Tk()

        #adjusting size of window and title
        self.main.geometry("480x480")
        self.main.title("Pizza Calculator")
        self.main.configure(bg='orange')

        #frames
        self.nameFrame = tkinter.Frame(self.main)
        self.topFrame = tkinter.Frame(self.main)
        self.midFrame = tkinter.Frame(self.main)
        self.bottomFrame = tkinter.Frame(self.main)

        self.nameFrame.configure(bg='orange')
        self.topFrame.configure(bg='orange')
        self.midFrame.configure(bg='orange')
        self.bottomFrame.configure(bg='orange')
    
        #main buttons
        self.calculate = tkinter.Button(self.bottomFrame,text="Calculate",command=self.calc)
        self.quit = tkinter.Button(self.bottomFrame,text="Quit",command=self.main.destroy)

        self.calculate.configure(bg='orange')
        self.quit.configure(bg='orange')
    
        #initializing variables
        self.pepperoniVar = tkinter.IntVar()
        self.sausageVar = tkinter.IntVar()
        self.pineappleVar = tkinter.IntVar()
        self.tomatoVar = tkinter.IntVar()
        
        self.pepperoniVar.set(0)
        self.sausageVar.set(0)
        self.pineappleVar.set(0)
        self.tomatoVar.set(0)

        self.thinCrustVar = tkinter.IntVar()
        self.thickCrustVar = tkinter.IntVar()
        self.deepDishVar = tkinter.IntVar()

        self.thinCrustVar.set(0)
        self.thickCrustVar.set(0)
        self.deepDishVar.set(0)

        #toppings
        self.blankLabel1 = tkinter.Label(self.topFrame, text="\n\n")
        self.toppingsLabel = tkinter.Label(self.topFrame, text="\n\nPlease select topping(s):")
        self.pepperoni = tkinter.Checkbutton(self.topFrame, text="Pepperoni", variable=self.pepperoniVar)
        self.sausage = tkinter.Checkbutton(self.topFrame, text="Sausage", variable=self.sausageVar)
        self.pineapple = tkinter.Checkbutton(self.topFrame, text="Pineapple", variable=self.pineappleVar)
        self.tomato = tkinter.Checkbutton(self.topFrame, text="Tomato", variable=self.tomatoVar)

        self.blankLabel1.configure(bg='orange')
        self.toppingsLabel.configure(bg='orange')
        self.pepperoni.configure(bg='orange')
        self.sausage.configure(bg='orange')
        self.pineapple.configure(bg='orange')
        self.tomato.configure(bg='orange')

        #crusts
        self.blankLabel2 = tkinter.Label(self.midFrame, text="\n\n")
        self.crustLabel =tkinter.Label(self.midFrame, text="\n\nPlease select a crust:")
        self.thinCrust = tkinter.Radiobutton(self.midFrame, text="Thin Crust", variable=self.thinCrustVar, value=1)
        self.thickCrust = tkinter.Radiobutton(self.midFrame, text="Thick Crust", variable=self.thickCrustVar, value=1)
        self.deepDish = tkinter.Radiobutton(self.midFrame, text="Deep Dish", variable=self.deepDishVar, value=1)

        self.blankLabel2.configure(bg='orange')
        self.crustLabel.configure(bg='orange')
        self.thinCrust.configure(bg='orange')
        self.thickCrust.configure(bg='orange')
        self.deepDish.configure(bg='orange')

        #name
        self.blankLabel3 = tkinter.Label(self.nameFrame, text="\n\n")
        self.nameLabel = tkinter.Label(self.nameFrame, text="Enter the name of the order:")
        self.nameBox = tkinter.Entry(self.nameFrame, width=20)
        
        self.blankLabel3.configure(bg='orange')
        self.nameLabel.configure(bg='orange')

        #pack
        self.nameFrame.pack(side="top")
        self.topFrame.pack(side="top")
        self.bottomFrame.pack(side="bottom")
        self.midFrame.pack(side="top")
        
        self.blankLabel3.pack(side="bottom")
        self.nameLabel.pack(side="top")
        self.nameBox.pack(side="top")

        self.calculate.pack(side="left")
        self.quit.pack(side="right")

        self.blankLabel2.pack(side="bottom")
        self.crustLabel.pack(side="top")
        self.thinCrust.pack(side="top")
        self.thickCrust.pack(side="top")
        self.deepDish.pack(side="top")

        self.blankLabel1.pack(side="bottom")
        self.toppingsLabel.pack(side="top")
        self.pepperoni.pack(side="top")
        self.sausage.pack(side="top")
        self.pineapple.pack(side="top")
        self.tomato.pack(side="top")

        tkinter.mainloop()

    #functions

    def calc(self):
        #initial
        self.message = 'Name: ' + self.nameBox.get() + '\n\n'
        self.total = 0
        #crust
        if self.thinCrustVar.get() == 1:
            self.message += "Thin Crust: $8.00\n"
            self.total += 8
        elif self.thickCrustVar.get() == 1:
            self.message += "Thick Crust: $10.00\n"
            self.total += 10
        elif self.deepDishVar.get() == 1:
            self.message += "Deep Dish: $12.00\n"
            self.total += 12
        #toppings
        if self.pepperoniVar.get() == 1:
            self.message += "Pepperoni: $0.30\n"
            self.total += .3
        if self.sausageVar.get() == 1:
            self.message += "Sausage: $0.45\n"
            self.total += .45
        if self.pineappleVar.get() == 1:
            self.message += "Pineapple: $0.35\n"
            self.total += .35
        if self.tomatoVar.get() == 1:
            self.message += "Tomato: $0.15\n"
            self.total += .15
        #message
        format(self.total, "5,.2f")
        self.totalMessage = self.message + "Total: $" + str(self.total)
        tkinter.messagebox.showinfo("Receipt", self.totalMessage)

pizCal = PizzaCalc()

print("moving on...")