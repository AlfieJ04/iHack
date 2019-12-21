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
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
from git import Repo

###################################################
#                                                 #
#                   ROOT WINDOW                   #
#                                                 #
###################################################

# Create and configure root window
root = Tk()
root.title("iHack")
root.iconbitmap('.assets/img/icon.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#root.configure(background='black')

# Create main frame

mainFrame = LabelFrame(root, text="This is the main frame!", padx=5, pady=5)

###################################################
#                                                 #
#                    FUNCTIONS                    #
#                                                 #
###################################################


# Update function
def updateClick():
    currentStatus = "Running update. Please wait"
    Repo.clone_from('https://github.com/AlfieJ04/iHack.git', '/opt/iHack')
    MsgBox = messagebox.showinfo('Update Complete','iHack updated!')

# Install function
def installClick():
    currentStatus = "Installing applications. Please wait"
    MsgBox = messagebox.askquestion ('Install Applications','Are you sure you want to install all applications?',icon = 'warning')
    if MsgBox == 'yes':
        subprocess.call("update.sh")
        MsgBox = messagebox.showinfo('Install Complete','All applications installed!')
    else:
        messagebox.showinfo('Install Cancelled','No applications were harmed in the making of this script')

# Quit function
def quitClick():
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
titleLabel = Label(root, text="iHack")
titleDescription = Label(root, text="The interactive hacking tool!")

# Button widgets
updateButton = Button(root, text="Update", padx=50, command=updateClick, bg="grey", fg="white")
installButton = Button(root, text="Install", padx=50, command=installClick, bg="grey", fg="white")
quitButton = Button(root, padx=50, text="Exit Program", command=quitClick, bg="grey", fg="white")

###################################################
#                                                 #
#                   STATUS BAR                    #
#                                                 #
###################################################

# Status Bar
currentStatus = ""
statusLabel = Label(root, text=str(currentStatus), bd=1, relief=SUNKEN, anchor=E)
statusLabel.grid(row=8, column=0, columnspan=7, sticky=W+E)

###################################################
#                                                 #
#                       GRID                      #
#                                                 #
###################################################

# Grid layout
titleLabel.grid(row=2, column=4, sticky="nsew")
titleDescription.grid(row=3, column=4, sticky="nsew")

# Buttons
updateButton.grid(row=5, column=1)
installButton.grid(row=5, column=2)
quitButton.grid(row=5, column=8)

###################################################
#                                                 #
#               ROOT WINDOW SPACING               #
#                                                 #
###################################################

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(9, weight=1)

###################################################
#                                                 #
#                     MAIN LOOP                   #
#                                                 #
###################################################

root.mainloop()