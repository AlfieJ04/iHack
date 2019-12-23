#!/usr/bin/python3

"""

iHack
An interactive hacking application
Created by AlfieJ04

"""
###################################################
#                                                 #
#                     IMPORTS                     #
#                                                 #
###################################################

import os
import time
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import tkinter.font
from PIL import ImageTk, Image
import subprocess
import socket
#from git import Repo


###################################################
#                                                 #
#                   ROOT WINDOW                   #
#                                                 #
###################################################

# Create and configure root window
root = Tk()
root.title("iHack")
if ( sys.platform.startswith('win')): 
    root.iconbitmap('.assets/img/icon.ico')
else:
    logo = PhotoImage(file='./.assets/img/logo.gif')
    root.call('wm', 'iconphoto', root._w, logo)

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu
subMenu = Menu(menubar, tearoff=0)

#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#root.configure(background='black')
titleFont = tkinter.font.Font(family = 'Verdana', size = 12, weight = "bold")
# Create main frame

mainFrame = LabelFrame(root, padx=5, pady=5)
mainFrame.pack()

###################################################
#                                                 #
#                    FUNCTIONS                    #
#                                                 #
###################################################

# Define progress bar
p = Progressbar(root,orient=HORIZONTAL,length=500,mode="determinate",takefocus=True,maximum=100)

# Function to display hostname and 
# IP address 
def get_Host_name_IP(): 
    try:
        f= open("IP.txt","w+") 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        f.write("Hostname :  ",host_name)
        f.write("IP : ",host_ip)
        
    except: 
        f.write("Unable to get Hostname and IP")

def get_info(arg):
    print (tfield.get("1.0", "current lineend"))

# Update function
def updateClick():
    statusLabel["text"] = "Running update. Please wait"
    gitCommand = 'git pull'
    #start_loading()
    process = subprocess.Popen(gitCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    #stop_loading()
    MsgBox = messagebox.showinfo('Update Complete','iHack updated!')
    statusLabel["text"] = "Update completed"

# Install function
def installClick():
    MsgBox = messagebox.askquestion ('Install Applications','Are you sure you want to install all applications?',icon = 'warning')
    if MsgBox == 'yes':
        statusLabel["text"] = "Installing applications. Please wait"
        #start_loading()
        subprocess.call(".scripts/update.sh")
        #stop_loading()
        MsgBox = messagebox.showinfo('Install Complete','All applications installed!')
        
    else:
        messagebox.showinfo('Install Cancelled','No applications were harmed in the making of this script')

# Monitor mode function
def monModeClick():
    statusLabel["text"] = "Enabling monitor mode. Please wait"
    subprocess.call(".scripts/airmon.sh")
    for i in range(100):                
        p.step()            
        root.update()
    MsgBox = messagebox.showinfo('Monitor Mode','Monitor mode enabled!')

# Quit function
def quitClick():
    statusLabel["text"] = "Quitting"
    MsgBox = messagebox.askquestion ('Exit App','Really Quit?',icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Welcome Back','Welcome back to the App')


###################################################
#                                                 #
#                    MENU BUTTONS                 #
#                                                 #
###################################################

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Install", command=updateClick)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About iHack', 'iHack is an interactive automated hacking application built using Python by @AlfieJ04')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)


###################################################
#                                                 #
#                      WIDGETS                    #
#                                                 #
###################################################


# Label widgets
titleLabel = Label(mainFrame, text="iHack", font=titleFont)
titleDescription = Label(mainFrame, text="The interactive hacking tool!", font=titleFont)

# Button widgets
updateButton = Button(mainFrame, text="Update iHack", padx=50, command=updateClick, bg="grey", fg="white")
installButton = Button(mainFrame, text="Install All", padx=50, command=installClick, bg="grey", fg="white")
monModeButton = Button(mainFrame, text="Monitor Mode", padx=50, command=monModeClick, bg="grey", fg="white")
quitButton = Button(mainFrame, padx=50, text="Exit Program", command=quitClick, bg="grey", fg="white")

###################################################
#                                                 #
#                 TERMINAL BOX                    #
#                                                 #
###################################################

termf = Frame(root, height=400, width=500, bg="black")
termf.pack(fill=BOTH, expand=YES)
tfield = Text(root)
get_Host_name_IP()
f= open("IP.txt","r")
for line in f:
    line = line.strip()
    if line:
        tfield.insert("end", line+"\n")
        # tfield.get("current linestart", "current lineend")
tfield.bind("<Return>", get_info)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

###################################################
#                                                 #
#                   STATUS BAR                    #
#                                                 #
###################################################

# Status Bar
statusLabel = Label(root, text="Welcome to iHack", bd=1, relief=SUNKEN, anchor=E, bg="grey", fg="white", font=titleFont)
#statusLabel.grid(row=8, column=1, columnspan=7, sticky=W+E)
statusLabel.pack(side=BOTTOM, fill=X, expand=1, pady=10)


###################################################
#                                                 #
#                       GRID                      #
#                                                 #
###################################################

# Grid 

#titleLabel.grid(row=2, column=4, sticky="nsew")
#titleDescription.grid(row=3, column=4, sticky="nsew")
titleLabel.pack(side=TOP)
titleDescription.pack(side=TOP)

# Buttons
#updateButton.grid(row=5, column=1)
#installButton.grid(row=5, column=2)
#quitButton.grid(row=5, column=8)

updateButton.pack(side=LEFT)
installButton.pack(side=LEFT)
monModeButton.pack(side=LEFT)
quitButton.pack(side=LEFT)

p.pack(pady=20)
###################################################
#                                                 #
#               ROOT WINDOW SPACING               #
#                                                 #
###################################################

#root.grid_rowconfigure(0, weight=1)
#root.grid_rowconfigure(9, weight=1)
#root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(9, weight=1)

###################################################
#                                                 #
#                     MAIN LOOP                   #
#                                                 #
###################################################

root.mainloop()
f.close()