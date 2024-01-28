from tkinter import *
import speedtest

# speed check function
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    # download speed in Mbps
    down = str(round(sp.download()/(10**6), 3)) + "Mbps"
    # upload speed in Mbps
    up = str(round(sp.upload()/(10**6), 3)) + "Mbps"
    
    lab_down.config(text= down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("400x500")
sp.config(bg="Grey")

# 
lab = Label(sp, text='Internet Speed Test', font=("Time New Roman", 20 ,"bold"), bg='grey', fg='white')
lab.place(x=50,y=10, height=50, width=300)

lab = Label(sp, text='Download Speed', font=("Time New Roman", 20 ,"bold"), bg='grey', fg='white')
lab.place(x=50,y=70, height=50, width=300)
lab_down = Label(sp, text='00', font=("Time New Roman", 20 ,"bold"))
lab_down.place(x=50,y=130, height=50, width=300)

lab = Label(sp, text='Upload Speed', font=("Time New Roman", 20 ,"bold"), bg='grey', fg='white')
lab.place(x=50,y=190, height=50, width=300)
lab_up = Label(sp, text='00', font=("Time New Roman", 20 ,"bold"))
lab_up.place(x=50,y=250, height=50, width=300)

# btn
btn = Button(sp, text='Check Speed', font=('Time New Roman', 20, 'bold'), relief='raised', command=speedcheck)
btn.place(x=100, y=320, height=50, width=200)


sp.mainloop()