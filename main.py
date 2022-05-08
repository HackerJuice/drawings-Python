from tkinter import *

root = Tk()
root.geometry('900x750')

myCanv = Canvas(root, width=900, height=750)
myCanv.pack()

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