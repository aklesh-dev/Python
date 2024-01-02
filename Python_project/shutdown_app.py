from tkinter import *
import os 

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 20')
def logout():
    os.system('shutdown -l')
def shutdown():
    os.system('shutdown /s /t 1')

st = Tk()
st.title("Shutdown App")
st.geometry("500x300")
st.config(bg="LightBlue")

# restart button
r_btn = Button(st, text="Restart", font=("Time New Romen",25,"bold"), relief=RAISED, cursor="exchange", command=restart)
r_btn.place(x=150, y=20, height=40, width=200)
# restart with time btn
rt_btn = Button(st, text="Restart with time", font=("Time New Romen",18,"bold"), relief=RAISED, cursor="exchange", command=restart_time)
rt_btn.place(x=150, y=80, height=40, width=200)
# logout btn
lg_btn = Button(st, text="Log-out", font=("Time New Romen",25,"bold"), relief=RAISED, cursor="target", command=logout)
lg_btn.place(x=150, y=140, height=40, width=200)
# shutdown btn
st_btn = Button(st, text="Shutdown", font=("Time New Romen",25,"bold"), relief=RAISED, cursor="mouse",command=shutdown)
st_btn.place(x=150, y=200, height=40, width=200)


st.mainloop()