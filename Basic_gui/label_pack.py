from tkinter import *

root=Tk()
# dimension
root.geometry("500x400")
root.title("MPV with GUI")

# Import Label option
option='''text- add the text
         \n bd- backround
         \n fg- foreground
         \n font- set the font size
         \n padx- x padding
          \n pady- y padding
          \n relief- border styling- SUNKEN,RAISED,GROOVE,RIDGE '''
t_l=Label(text=option,bg='red',fg='white',
          font=("Helvetica", 10, "bold italic"),
          padx=200,pady=94,relief=GROOVE)
# Import pack options
''' anchor- nw,ne,se,sw
    side=top,buttom,left,right
    fill=x,y
    padding=padx,pady
    '''

t_l.pack(fill='x',side='top')


root.mainloop()
