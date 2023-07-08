from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
import random

window = Tk()
window.geometry("800x400")

dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = Label(window, image=image1)
label2 = Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x=0, y=100)
label2.place(x=200, y=100)
def dice_roll_fun():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2
button = Button(window, text='Roll the dice', bg='blue', fg='white', command=dice_roll_fun)
button.place(x=120, y=300)
window.mainloop()
