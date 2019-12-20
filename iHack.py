import os
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
from git import Repo

root = Tk()
root.title("iHack")
root.iconbitmap('.assets/img/icon.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#root.configure(background='black')


# Update function
def updateClick():
    currentStatus = "Running update. Please wait"
    Repo.clone_from('https://github.com/AlfieJ04/iHack.git', '/opt/iHack')
    subprocess.call("update.sh")
    MsgBox = messagebox.showinfo('Update Complete','All applications updated!')

# Quit function
def quitClick():
    MsgBox = messagebox.askquestion ('Exit App','Really Quit?',icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Welcome Back','Welcome back to the App')

# Label widgets
titleLabel = Label(root, text="iHack")
titleDescription = Label(root, text="The interactive hacking tool!")

# Button widgets
updateButton = Button(root, text="Update", padx=50, command=updateClick, bg="grey", fg="white")
quitButton = Button(root, text="Exit Program", command=quitClick, bg="grey", fg="white")

# Show widgets on the screen

currentStatus = ""
statusLabel = Label(root, text=str(currentStatus), bd=1, relief=SUNKEN, anchor=E)


titleLabel.grid(row=2, column=4, sticky="nsew")
titleDescription.grid(row=3, column=4, sticky="nsew")
updateButton.grid(row=5, column=1)
quitButton.grid(row=5, column=8)
statusLabel.grid(row=8, column=0, columnspan=9, sticky=W+E)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(9, weight=1)

root.mainloop()