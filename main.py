from tkinter import *
import time
import sys

w = 800
h = 500
s = 50
mx = 0
my = 0
active = True

tk = Tk()

canvas = Canvas(tk, width=w, height=h, bg="grey")
canvas.pack()
color = 'black'


class Gui:
    x, y = 0, 0

    def __init__(self, x, y):
        self.shape = canvas.create_rectangle(x, y, s, y+s, fill='white')
        self.update()
        Gui.x = x
        Gui.y = y

    def update(self):
        pos = canvas.coords(self.shape)
        print(pos)
        if pos[2] >= mx >= pos[0]:
            print('hit')
            active = False
        else:
            active = True
        if pos[3] >= my >= pos[1]:
            print('hit')
            active = False
        else:
            active = True


class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, s, s, fill=color)
        self.sx = 3
        self.sy = 3
        self.move()

    def update(self):
        canvas.move(self.shape, self.sx, self.sy)
        pos = canvas.coords(self.shape)
        if pos[2] >= w or pos[0] <= 0:
            self.sx *= -1
        if pos[3] >= h - s or pos[1] <= 0:
            self.sy *= -1

    def move(self):
        if active:
            self.update()
            tk.after(20, self.move)


def motion(event):
    mx = event.x
    my = event.y
    print(mx, my)


def main():
    ball = Ball()
    g = Gui(0, h - s)
    tk.bind('<Motion>', motion)
    tk.mainloop()


if __name__ == "__main__":
    main()
