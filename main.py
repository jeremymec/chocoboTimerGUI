from tkinter import *
from Timer import *
from PIL import Image, ImageTk

class Window:
    def __init__(self, master):
        self.master = master
        self.timer = Timer()

        master.wm_attributes('-transparentcolor', 'black')

        master.title("Chocobo Timer")

        master.minsize(width="400", height="500")

        self.addTimerButton = Button(master, text="Fed", command=self.createTimer)
        self.addTimerButton.pack(side="bottom")

        self.timerLabels = []

        self.update()

    def update(self):
        for timer in self.timer.timerList:
            obj = self.checkTimer(timer)
            if obj is not None:
                self.updateTimer(obj)
            else:
                self.addTimer(timer)

        for obj in self.timerLabels:
            if obj.timer not in self.timer.timerList:
                print("TBA")

        PyTimer(1, self.update).start()

    def checkTimer(self, timer):
        for obj in self.timerLabels:
            if obj.timer == timer:
                return obj

    def updateTimer(self, labelObj):
        labelObj.frame.itemconfig(labelObj.text, text=self.processTime(labelObj.timer), font=(None, 22))

    def addTimer(self, timer):
        PNGImage = Image.open("Frame.png")
        frameImage = ImageTk.PhotoImage(PNGImage)

        frame = Canvas(self.master, width=300, height=75)
        frame.pack(anchor="w")

        frame.create_image(0, 0, image=frameImage, anchor=NW)
        frame.pack_propagate(0)

        label = frame.create_text(150, 10, anchor="n")
        frame.itemconfigure(label, text="Timer " + str(timer[3]))

        text = frame.create_text(8, 40, anchor="w")
        frame.itemconfigure(text, text=self.processTime(timer), font=(None, 22))

        self.timerLabels.append(TimerObject(timer, label, frame, text))

    def processTime(self, timer):
        started = timer[1]
        deltaT = time.time() - started
        remain = timer[2] - deltaT

        minutes, seconds = divmod(remain, 60)
        minutes = int(minutes)
        seconds = int(seconds)

        minutes = str(minutes)
        seconds = str(seconds)

        if len(minutes) == 1:
            minutes = "0" + minutes

        if len(seconds) == 1:
            seconds = "0" + seconds

        return str(minutes) + ":" + str(seconds)

    def createTimer(self):
        self.timer.startTimer(10)


class TimerObject(object):
    def __init__(self, timer, label, frame, text):
        self.timer = timer
        self.label = label
        self.frame = frame
        self.text = text


if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()
