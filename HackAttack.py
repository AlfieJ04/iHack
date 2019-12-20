from tkinter import *

root = Tk()
root.title("Hack-Attack")
root.iconbitmap('.assets/img/icon.ico')
#root.geometry("500x500+0+0")
#frmMain = Frame(root,bg="grey")


# Update function
def updateClick():
    updateLabel = Label(root, text="Running update. Please wait")
    updateLabel.grid(row=7, column=4)


# Label widgets
titleLabel = Label(root, text="Hack-Attack")
titleDescription = Label(root, text="The ultimate hacking tool!")
spacerLabel = Label(root, text="        ")
# Button widgets
updateButton = Button(root, text="Update", padx=50, command=updateClick, bg="grey", fg="white")

# Show widgets on the screen

titleLabel.grid(row=1, column=4, sticky="nsew")
titleDescription.grid(row=2, column=4, sticky="nsew")
updateButton.grid(row=5, column=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(9, weight=1)

root.mainloop()