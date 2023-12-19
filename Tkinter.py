from tkinter import *

root = Tk()

root.geometry("200x150")


button = Button(root, text="Click me!", command=print("click!"), bg = "red")
stopbutton = Button(root, text="quit", command=root.destroy)

button.pack()
stopbutton.pack()

root.mainloop()