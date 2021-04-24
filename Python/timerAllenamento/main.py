from PIL import ImageTk, Image
from tkinter import Label
from playsound import playsound
import tkinter as tk
import time

win = tk.Tk()
win.title('Circuito Brucia Calorie | Allenamento')
win.geometry("550x650")


def timerAllenati():
    timer = 20
    while timer:
        time.sleep(1)
        timer -= 1
    playsound("src/audio/Pause.mp3")


def pausa():
    timer = 10
    while timer:
        time.sleep(1)
        timer -= 1
    playsound("src/audio/Start.mp3")


def allenamentoCalorie():
    i = 0
    pausa()
    while i < 24:
        timerAllenati()
        pausa()
        i = i + 1
    playsound("src/audio/Finish.mp3")


# Main
title = Label(win, text="Circuito Brucia Calorie | Allenamento", font=("Times", 20, "bold"))
title.grid(row=1, column=2, columnspan=5, padx=30, pady=10)
img = Image.open("src/img/img.jpg")
img = img.resize((500, 500), Image.ANTIALIAS)
resized_img = ImageTk.PhotoImage(img)

image = tk.Label(win, image=resized_img)
image.grid(row=2, column=0, columnspan=5, pady=20)
btn = tk.Button(win, text="Allenati", command=allenamentoCalorie)
btn.grid(row=4, column=0, columnspan=5, pady=10)

win.mainloop()
