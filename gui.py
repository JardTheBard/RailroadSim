from tkinter import *
import os

class userGui:
    def __init__(self):

        self.serverIp = ""
        self.locoAddress = ""
        ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
        INFO = os.path.join(ROOT_FOLDER, 'info.txt')
        IMAGE = os.path.join(ROOT_FOLDER, 'choochoo.gif')

        window = Tk()

        def manualClicked():
            global serverIp
            global locoAddress
            serverIp = txt1.get()
            locoAddress = txt2.get()
            f = open(INFO,'w')
            f.write(serverIp + '\n')
            f.write(locoAddress)

            if ((serverIp != "") and (locoAddress != "")):
                f.close()
                window.destroy()
        
        def fileClicked():
            global serverIp
            global locoAddress
            f = open(INFO,'r')
            serverIp = f.readline()
            serverIp = serverIp.rstrip('\n')
            locoAddress = f.readline()
            locoAddress = locoAddress.rstrip('\n')
            f.close()
            window.destroy()
        
        window.title("Enter IP and Address")
        
        window.geometry('310x130')

        prompt1 = Label(window, text="Enter Server IP: ")
        prompt1.grid(column=1, row=1)

        prompt2 = Label(window, text="Enter Locomotive Address: ")
        prompt2.grid(column=1, row=2)
        
        txt1 = Entry(window,width=15)
        txt1.grid(column=2, row=1)
        txt1.focus_set()

        txt2 = Entry(window,width=15)
        txt2.grid(column=2, row=2)
        
        btn1 = Button(window, text="Manual Input", command=manualClicked) 
        btn1.grid(column=2, row=3)

        btn2 = Button(window, text="Previous Input", command=fileClicked) 
        btn2.grid(column=1, row=3)

        f = open(INFO,'r')
        tempIP = f.readline()
        tempIP= tempIP.rstrip('\n')
        tempAdr = f.readline()
        tempAdr = tempAdr.rstrip('\n')

        lastIP = Label(window, text="Previous IP Address: " + tempIP)
        lastIP.grid(column=1, row=4, pady=(10,0))

        lastAdr = Label(window, text="Previous Locomotive Address: " + tempAdr)
        lastAdr.grid(column=1, row=5)

        window.mainloop()

    def returnValues(self):
        global serverIp
        global locoAddress
        return serverIp, locoAddress
