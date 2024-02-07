from tkinter import *


aken = Tk()
aken.title("Sinu nimi")
aken.resizable(0, 0)
aken.configure(background='black')
tekst = Label(aken,
              pady="20",
              padx="20",
              fg="red",
              bg="black",
              font="Tahoma 16 bold italic",
              text="Nimi: Karin Eergreid\nRühm: IT23\n2024").pack()

aken.mainloop()