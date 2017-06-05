from threading import Timer as PyTimer
import time


class Timer:

    timerList = []
    timerCount = 0

    def ding(self):
        print("ding")
        self.updateList()

    def updateList(self):
        for timerData in self.timerList:
            started = timerData[1]
            deltaT = time.time() - started
            remain = timerData[2] - deltaT

            if remain <= 0:
                print("Timer Removed")
                self.timerList.remove(timerData)
                self.timerCount -= 1

    def startTimer(self, timeLength):
        self.timerCount += 1
        t = PyTimer(timeLength, self.ding)
        t.start()
        # Timer Object, Time Started, Length of Timer, Count of Timer, Label Boolean, Active Boolean
        tData = [t, time.time(), timeLength, self.timerCount]
        self.timerList.append(tData)
