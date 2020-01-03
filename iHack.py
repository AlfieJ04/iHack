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
import logging
#from git import Repo

###################################################
#                                                 #
#                     LOGGING                     #
#                                                 #
###################################################

logging.basicConfig(level=logging.DEBUG, filename="logfile.txt", filemode="w+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
#lf = open("logfile.txt", "a")
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
pb = Progressbar(root,orient=HORIZONTAL,length=500,mode="determinate",takefocus=True,maximum=100)

# Function to display hostname and IP address 
def get_Host_name_IP(): 
    try:
        #lf = open("logfile.txt","a") 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        logging.info(f"Hostname :  {host_name}")
        logging.info(f"IP : {host_ip}")
    except Exception as ex: 
        print(ex) 
        logging.info(ex)


def get_info(arg):
    #print (tfield.get("1.0", "current lineend"))
    logging.info(tfield.get("1.0", "current lineend"))

# Update function
def updateClick():
    statusLabel["text"] = "Running update. Please wait"
    gitCommand = 'git pull'
    lf = open("logfile.txt", "a")
    process = subprocess.Popen(gitCommand.split(), stdout=lf)
    output, error = process.communicate()
    MsgBox = messagebox.showinfo('Update Complete','iHack updated!')
    statusLabel["text"] = "Update completed"
    logging.info(f"Update complete, iHack was updated!")

# Install function
def installClick():
    MsgBox = messagebox.askquestion ('Install Applications','Are you sure you want to install all applications?',icon = 'warning')
    if MsgBox == 'yes':
        statusLabel["text"] = "Installing applications. Please wait"
        lf = open("logfile.txt", "a")
        process = subprocess.Popen(['sh','.scripts/update.sh'], stdout=lf)
        output, error = process.communicate()
        MsgBox = messagebox.showinfo('Install Complete','All applications installed!')
        logging.info(f"Install complete, All applications installed!")
    else:
        messagebox.showinfo('Install Cancelled','No applications were harmed in the making of this script!')
        logging.info(f"Install cancelled','No applications were harmed in the making of this script!")
        

# Monitor mode function
def monModeClick():
    statusLabel["text"] = "Enabling monitor mode. Please wait"
    #subprocess.call(".scripts/airmon.sh")
    lf = open("logfile.txt", "a")
    process = subprocess.Popen(['sh','.scripts/airmon.sh'], stdout=lf)
    output, error = process.communicate()
    MsgBox = messagebox.showinfo('Monitor Mode','Monitor mode enabled!')
    statusLabel["text"] = "Monitor mode enabled"
    logging.warning(f"Monitor mode enabled!")

# Quit function
def quitClick():
    statusLabel["text"] = "Quitting"
    MsgBox = messagebox.askquestion ('Exit App','Really Quit?',icon = 'error')
    if MsgBox == 'yes':
        logging.warning(f"Quitting iHack!\n")
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

tfield = Text(root, bg='black', fg='white')
tfield.pack(fill=BOTH, expand=YES)
get_Host_name_IP()
log = open("logfile.txt","r")
for line in log:
    line = line.strip()
    if line:
        tfield.insert("end", line+"\n")
        # tfield.get("current linestart", "current lineend")
tfield.bind("<Return>", get_info)


###################################################
#                                                 #
#                   STATUS BAR                    #
#                                                 #
###################################################

# Status Bar
statusLabel = Label(root, text="Welcome to iHack", bd=1, relief=SUNKEN, anchor=E, bg="grey", fg="white", font=titleFont)
statusLabel.pack(side=BOTTOM, fill=X, expand=1, pady=10)


###################################################
#                                                 #
#                     LAYOUT                      #
#                                                 #
###################################################

titleLabel.pack(side=TOP)
titleDescription.pack(side=TOP)

updateButton.pack(side=LEFT)
installButton.pack(side=LEFT)
monModeButton.pack(side=LEFT)
quitButton.pack(side=LEFT)

pb.pack(pady=20)

###################################################
#                                                 #
#                     MAIN LOOP                   #
#                                                 #
###################################################

root.mainloop()
log.close()
