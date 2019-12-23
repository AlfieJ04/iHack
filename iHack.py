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
import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Button, Tk, HORIZONTAL
from PIL import ImageTk, Image
import subprocess
#from git import Repo

# Set currentStatus
currentStatus = "Waiting for input"

###################################################
#                                                 #
#                   ROOT WINDOW                   #
#                                                 #
###################################################

# Create and configure root window
root = Tk()
root.title("iHack")
root.iconbitmap('icon.ico')
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#root.configure(background='black')
titleFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
# Create main frame

mainFrame = LabelFrame(root, padx=5, pady=5)
mainFrame.pack()
###################################################
#                                                 #
#                    FUNCTIONS                    #
#                                                 #
###################################################


# Update function
def updateClick():
    currentStatus = "Running update. Please wait"
    root.update()
    gitCommand = "cd /opt/iHack && git pull"
    process = subprocess.Popen(gitCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    MsgBox = messagebox.showinfo('Update Complete','iHack updated!')

# Install function
def installClick():
    MsgBox = messagebox.askquestion ('Install Applications','Are you sure you want to install all applications?',icon = 'warning')
    if MsgBox == 'yes':
        currentStatus = "Installing applications. Please wait"
        root.update()
        subprocess.call("update.sh")
        MsgBox = messagebox.showinfo('Install Complete','All applications installed!')
        
    else:
        messagebox.showinfo('Install Cancelled','No applications were harmed in the making of this script')

# Quit function
def quitClick():
    currentStatus = "Quitting"
    MsgBox = messagebox.askquestion ('Exit App','Really Quit?',icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Welcome Back','Welcome back to the App')


###################################################
#                                                 #
#                      WIDGETS                    #
#                                                 #
###################################################


# Label widgets
titleLabel = Label(mainFrame, text="iHack", font=titleFont)
titleDescription = Label(mainFrame, text="The interactive hacking tool!", font=titleFont)

# Button widgets
updateButton = Button(mainFrame, text="Update", padx=50, command=updateClick, bg="grey", fg="white")
installButton = Button(mainFrame, text="Install", padx=50, command=installClick, bg="grey", fg="white")
quitButton = Button(mainFrame, padx=50, text="Exit Program", command=quitClick, bg="grey", fg="white")

###################################################
#                                                 #
#                   STATUS BAR                    #
#                                                 #
###################################################

# Status Bar
statusLabel = Label(root, text=str(currentStatus), bd=1, relief=SUNKEN, anchor=E, bg="grey", fg="white", font=titleFont)
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
quitButton.pack(side=LEFT)

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