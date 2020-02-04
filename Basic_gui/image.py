from tkinter import *

root=Tk()
# dimension
root.geometry("500x400")
root.title("MPV with GUI")

# path of image
path="mpv_pic.png"

# for png pic
img = PhotoImage(file=path)
label=Label(image=img)
label.pack()


root.mainloop()
