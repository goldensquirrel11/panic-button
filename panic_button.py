import tkinter as tk
import tkinter.ttk as ttk
import serial
import time
from PIL import ImageTk
import concurrent.futures

class window:
    '''
    gui class
    '''
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        # configure root window
        top.geometry("626x921+631+53")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Panic app")
        top.configure(background="#b4fef4")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        # Deco.creation logo
        self.logo = ttk.Label(top)
        self.logo.place(relx=0.319, rely=0.022, height=205, width=205)
        self.logo.configure(background="#b4fef4")
        self.logo.configure(foreground="#000000")
        self.logo.configure(relief="flat")
        self.logo.configure(anchor='center')
        self.logo.configure(justify='center')
        global _img0
        _img0 = ImageTk.PhotoImage(file='images/5005.JPG')
        self.logo.configure(image=_img0)
        self.logo.configure(compound='center')
        self.logo.configure(state='active')

        # Panic status
        self.status = tk.Label(top)
        self.status.place(relx=0.128, rely=0.293, height=106, width=442)
        self.status.configure(activebackground="#f9f9f9")
        self.status.configure(activeforeground="black")
        self.status.configure(background="#80ffff")
        self.status.configure(disabledforeground="#a3a3a3")
        self.status.configure(font="-family {Terminal} -size 24 -weight bold")
        self.status.configure(foreground="#f5010a")
        self.status.configure(highlightbackground="#d9d9d9")
        self.status.configure(highlightcolor="black")

        # connection label
        self.connection_label = tk.Label(top)
        self.connection_label.place(relx=0.016, rely=0.597, height=56, width=202)
        self.connection_label.configure(activebackground="#f9f9f9")
        self.connection_label.configure(activeforeground="black")
        self.connection_label.configure(background="#acc5d5")
        self.connection_label.configure(disabledforeground="#a3a3a3")
        self.connection_label.configure(font="-family {Segoe UI} -size 14")
        self.connection_label.configure(foreground="#000000")
        self.connection_label.configure(highlightbackground="#d9d9d9")
        self.connection_label.configure(highlightcolor="black")
        self.connection_label.configure(text='''Connection status:''')

        # bluetooth connection status
        self.connection_status = tk.Label(top)
        self.connection_status.place(relx=0.335, rely=0.597, height=56
                , width=412)
        self.connection_status.configure(activebackground="#f9f9f9")
        self.connection_status.configure(activeforeground="black")
        self.connection_status.configure(background="#acc5d5")
        self.connection_status.configure(disabledforeground="#a3a3a3")
        self.connection_status.configure(font="-family {Unispace} -size 18 -weight bold")
        self.connection_status.configure(foreground="#000000")
        self.connection_status.configure(highlightbackground="#d9d9d9")
        self.connection_status.configure(highlightcolor="black")

# initiate tkinter root window
root = tk.Tk()
top = window(root)

# update connection status
top.connection_status['text'] = 'connecting...'

# retries port connection until successful
while True:
    try:
        root.update()
        serRx = serial.Serial(port='COM6', baudrate=9600, timeout=0.01)
        top.connection_status['text'] = 'connection successful'
        break
    except:
        print('retrying bluetooth connection...')

# check which port was really used
print(serRx.name)
print()

# reads bluetooth port in an infinite loop
while True:
    a = serRx.readline()
    if a:
        print(a)
        print('PANIC')
        top.status['text'] = 'PANIC DETECTED'
        root.update()
        time.sleep(1)
        top.status['text'] = ''
    root.update()