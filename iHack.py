from tkinter import *
from PIL import ImageTk, Image
import subprocess



root = Tk()
root.title("Hack-Attack")
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
    subprocess.run(["sudo", "git", "clone", "https://github.com/AlfieJ04/iHack.git", "/opt/iHack/"])
    Tk.messagebox.showinfo("Update Complete", "iHack application update completed")


# Label widgets
titleLabel = Label(root, text="iHack")
titleDescription = Label(root, text="The interactive hacking tool!")

# Button widgets
updateButton = Button(root, text="Update", padx=50, command=updateClick, bg="grey", fg="white")
quitButton = Button(root, text="Exit Program", command=root.quit)
Tk.messagebox.askyesno("Quit", "Quit?")
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