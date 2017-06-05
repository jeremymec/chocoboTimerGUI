from tkinter import Tk, Button
from threading import Timer as PyTimer
from Timer import *


class Window:
    def __init__(self, master):
        self.master = master
        self.timer = Timer()

        master.title("Chocobo Timer")

        self.addTimerButton = Button(master, text="Fed", command=self.timer.startTimer(10))
        self.addTimerButton.pack()

        self.update()

    def update(self):
        print("Tick")
        PyTimer(1, self.update).start()

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()
