from threading import Timer as PyTimer
import time


class Timer:

    timerList = []
    timerCount = 0

    def ding(self):
        print("ding")

    def updateList(self):
        for timerData in self.timerList:
            started = timerData[1]
            deltaT = time.time() - started
            remain = timerData[2] - deltaT

            if remain <= 0:
                self.timerList.remove(timerData)
                self.timerCount -= 1

    def startTimer(self, timeLength):
        self.timerCount += 1
        t = PyTimer(timeLength, self.ding)
        t.start()
        tData = [t, time.time(), timeLength, self.timerCount]
        self.timerList.append(tData)
