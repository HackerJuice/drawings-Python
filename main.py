from tkinter import *

root = Tk()
root.geometry('900x850')

myCanv = Canvas(root, width=900, height=750)
myCanv.pack()

def change_size(length):
    global size
    size = int(length)

mySizeE = Entry(root)
mySizeE.pack(); mySizeE.insert(0, 'Enter Size: ')

mySize = Button(root, text = 'Change Size', command=lambda: change_size(mySizeE.get()))
mySize.pack()

size = 10

old_x, old_y = None, None

def reset(e):
    global old_x, old_y

    old_x, old_y = None, None


def draw(e):
    global old_x, old_y, myCanv

    if (old_x and old_y):
        myCanv.create_line(old_x, old_y, e.x, e.y, capstyle=ROUND)

    old_x, old_y = e.x, e.y

root.bind('<B1-Motion>', draw)
root.bind('<Motion>', reset)

root.mainloop()