#! python3
import pyautogui, time
from threadsafe_tkinter import *

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

class idleWindow:

    def __init__(self, master):
        self.master = master
        self.button_clicks = 0

        self.labelText = StringVar()
        self.labelText.set("Idle Stopped.")
        self.idleStatus = Label(master, textvariable=self.labelText)
        self.idleStatus.pack(side=RIGHT)

        #self.startButton = Button(master, text="Start Idle", command=self.startIdle)
        #self.startButton.pack(side=LEFT)

        self.startStopButton = Button(master, text='Start/Stop', command=self.startStopButton)
        self.startStopButton.pack(side=LEFT)

    def startIdle(self):
            #self.labelText.set("Idle is Running...")
            #self.pauseButton.config(state=NORMAL)
            self.idleStatus.update_idletasks()
            pyautogui.typewrite(['numlock', 'numlock'])
            print("Working...")
            self.after_id = self.master.after(5000, self.startIdle)

    def startStopButton(self):
        self.button_clicks += 0
        self.labelText.set("Idle is Running = " + str(self.button_clicks))
        self.startStopButton['text'] = "Start"
        if self.button_clicks == 0:
            self.button_clicks += 1
            self.startStopButton['text'] = "Started " + str(self.button_clicks)
            self.startIdle()
        else:
            self.labelText.set("Idle is Paused." + str(self.button_clicks))
            self.startStopButton['text'] = 'Paused ' + str(self.button_clicks)
            self.stopIdle()
            self.idleStatus.update_idletasks()
            self.button_clicks = 0


root = Tk()
root.geometry("380x50+0+945")
root.title("Idle")
runWindow = idleWindow(root)
root.mainloop()
