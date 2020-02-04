
from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text



root = Tk()
root.title(" News - Aapka Apna Akhabaar")
root.geometry("1000x600")

texts = []
photos = []
for i in range(0, 2):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((400, 200), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Mateshwari News", font="lucida 34 bold").pack()
Label(f0, text="January 19, 2050", font="lucida 16 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=200, pady=14,padx=134)
Label(f1, text=texts[0], padx=22, pady=22,font="lucida 8 bold").pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22,font="lucida 9 bold").pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")







root.mainloop()
