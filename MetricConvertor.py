from tkinter import Tk, Canvas, Button, CENTER, \
Label, HORIZONTAL, StringVar, DoubleVar, Entry, NW

class Convertor():

    def gui(self):
        root = Tk()
        root.title("Metric Convertor.")
        root.geometry("600x400+350+50")
        root.configure(bg="white")
        title = Label(root,text="Metric Convertor",justify=CENTER,
                      font=("Arial",25),bg="white",pady="20")
        title.grid(column=2,row=0)

        def close():
            root.destroy()

        close = Button(root,text="Quit",justify=CENTER,command=close)
        close.grid(column=3,row=15,pady=10,ipadx=15)

        #CONVERT CELSIUS TO FAHRENHEIT
        convert2fahrenheit = Label(root,text="Celsius to Farhenhiet",
                                   font=("Arial",12),bg="white"
                                   ,padx=25,justify=CENTER)
        convert2fahrenheit.grid(column=1,row=1)

        def showCelsius():
            result = (float(entry4fahrenheit.get()) * 9/5) + 32
            resultDisplay = Label(root,text=f"{str(result)} fahrenheit.",pady=10,bg="white").grid(column=2,row=2)
            return

        entry4fahrenheit = Entry(root,bd=3,justify=CENTER)
        entry4fahrenheit.grid(column=2,row=1)

        fahrenheitButton = Button(root,text="Calculate",command=showCelsius,justify=CENTER)
        fahrenheitButton.grid(column=3,row=1,pady=10)
        #-----------------------------------------------------------------------------------

        # CONVERT FAHRENHEIT TO CELSIUS
        convert2celsius = Label(root,text="Fahrenhiet to Celsius",
                                   font=("Arial",12),bg="white"
                                   ,padx=25,justify=CENTER)
        convert2celsius.grid(column=1,row=3)

        def showFahrenheit():
            result = round((float(entry4celsius.get()) - 32) * 5/9,1)
            resultDisplay = Label(root, text=f"{str(result)} celsius.", pady=10, bg="white").grid(column=2, row=4)

        entry4celsius = Entry(root, bd=3, justify=CENTER)
        entry4celsius.grid(column=2, row=3)

        celsiusButton = Button(root, text="Calculate", command=showFahrenheit,justify=CENTER)
        celsiusButton.grid(column=3, row=3, pady=10)
        # -----------------------------------------------------------------------------------

        # CONVERT METRES TO FEET
        metres2feet = Label(root,text="Metres to Feet",bg="white",
                            font=("Arial",12),padx=25, justify=CENTER)
        metres2feet.grid(column=1,row=5)

        def showFoot():
            result = round(float(entry4metres.get())*3.281,1)
            resultDisplay = Label(root,text=f"{str(result)} foot.", pady=10, bg="white").grid(column=2,row=6)

        entry4metres = Entry(root,bd=3,justify=CENTER)
        entry4metres.grid(column=2,row=5)

        feetButton = Button(root, text="Calculate", command=showFoot, justify=CENTER)
        feetButton.grid(column=3, row=5, pady=10)
        # -----------------------------------------------------------------------------------

        # CONVERT FEET TO METRES.

        feet2metres = Label(root,text="Feet to Metres", bg="white",
                            font=("Arial",12),padx=25,justify=CENTER)
        feet2metres.grid(column=1,row=7)

        def showMetres():
            result = round(float(entry4feet.get()) / 3.281, 2)
            resultDisplay = Label(root, text=f"{str(result)} metres.", pady=10, bg="white").grid(column=2, row=8)

        entry4feet = Entry(root,bd=3,justify=CENTER)
        entry4feet.grid(column=2,row=7)

        metresButton = Button(root,text='Calculate',command=showMetres, justify=CENTER)
        metresButton.grid(column=3,row=7,pady=10)

        # -----------------------------------------------------------------------------------

        # CONVERT KILOGRAMS TO POUNDS.

        kgToPounds = Label(root, text="Kilograms to Pounds", bg="white",
                            font=("Arial", 12), padx=25, justify=CENTER)
        kgToPounds.grid(column=1, row=9)

        def showPounds():
            result = round(float(entry4Kg.get()) * 2.205, 2)
            resultDisplay = Label(root, text=f"{str(result)} pounds.", pady=10, bg="white").grid(column=2, row=10)

        entry4Kg = Entry(root, bd=3, justify=CENTER)
        entry4Kg.grid(column=2, row=9)

        poundsButton = Button(root, text='Calculate', command=showPounds, justify=CENTER)
        poundsButton.grid(column=3, row=9, pady=10)

        # -----------------------------------------------------------------------------------

        poundsToKg = Label(root, text="Pounds to Kilograms", bg="white",
                           font=("Arial", 12), padx=25, justify=CENTER)
        poundsToKg.grid(column=1, row=11)

        def showKilograms():
            result = round(float(entry4Pounds.get()) / 2.205, 2)
            resultDisplay = Label(root, text=f"{str(result)} kilograms.", pady=10, bg="white").grid(column=2, row=12)

        entry4Pounds = Entry(root, bd=3, justify=CENTER)
        entry4Pounds.grid(column=2, row=11)

        kiloButton = Button(root, text='Calculate', command=showKilograms, justify=CENTER)
        kiloButton.grid(column=3, row=11, pady=10)

        entry4Pounds.bind('<Return>',lambda x: showKilograms())
        entry4Kg.bind('<Return>', lambda x: showPounds())
        entry4feet.bind('<Return>', lambda x: showMetres())
        entry4celsius.bind('<Return>', lambda x: showFahrenheit())
        entry4metres.bind('<Return>', lambda x: showFoot())
        entry4fahrenheit.bind('<Return>', lambda x: showCelsius())


        root.mainloop()

def main():

    application = Convertor()
    application.gui()

if __name__ == "__main__":
    main()

