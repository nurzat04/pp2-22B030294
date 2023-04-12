import random
from tkinter import *
from tkinter.colorchooser import askcolor

class Painter:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.old_x, self.old_y = None, None
        self.color = "black"
        self.line_width = 1
        self.eraser_on = False
        self.rect_on = True
        
        self.setup()
        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_end_x = None
        self.rect_end_y = None

        self.circ_start_x = None
        self.circ_start_y = None
        self.circ_end_x = None
        self.circ_end_y = None
        self.circ_on = False

        

    def setup(self):
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen)
        self.pen_button.pack(side=LEFT)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush)
        self.brush_button.pack(side=LEFT)

        self.color_button = Button(self.root, text='Color', command=self.choose_color)
        self.color_button.pack(side=LEFT)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.pack(side=LEFT)

        self.clear_button = Button(self.root, text='Clear', command=self.clear_canvas)
        self.clear_button.pack(side=LEFT)
        
        self.rectangle_button = Button(self.root, text='Rectangle', command=self.draw_rectangle)
        self.rectangle_button.pack(side=LEFT)  # Add random rectangle button
        
        self.circle_button = Button(self.root, text='Circle', command=self.draw_circle)
        self.circle_button.pack(side=LEFT)
        
    def use_pen(self):
        self.eraser_on = False
        self.eraser_on = False

    def use_brush(self): 
        self.eraser_on = False
        self.eraser_on = False

    def choose_color(self):
        self.eraser_on = False
        
        self.color = askcolor()[1]
    def use_eraser(self):
        self.canvas.bind("<B1-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_erase)

    def erase(self, event):
        x, y = (event.x, event.y)
        self.canvas.create_oval(x, y, x + self.line_width, y + self.line_width, fill="white", outline="white")
    def stop_erase(self, event):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
    def paint(self, event):
        if self.old_x and self.old_y:
            if self.eraser_on:
                self.canvas.create_line(event.x, event.y, self.old_x, self.old_y, width=self.line_width, fill='white')
            else:
                self.canvas.create_line(event.x, event.y, self.old_x, self.old_y, width=self.line_width, fill=self.color)
        self.old_x, self.old_y = event.x, event.y

    def reset(self,event):
        self.old_x, self.old_y = None, None
        self.canvas.delete("temp_rect", "temp_circ")

    def clear_canvas(self):
        self.canvas.delete(ALL)

    def draw_rectangle(self):
        self.rect_on = True
        self.canvas.bind("<ButtonPress-1>", self.start_rect)

    def start_rect(self, event):
        self.rect_start_x = event.x
        self.rect_start_y = event.y
        self.canvas.bind("<B1-Motion>", self.draw_rect)
        self.canvas.bind("<ButtonRelease-1>", self.stop_rect)

    def draw_rect(self, event):
        self.rect_end_x = event.x
        self.rect_end_y = event.y
        self.canvas.delete("temp_rect")
        self.canvas.create_rectangle(self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y, outline=self.color, width=self.line_width, tags="temp_rect")

    def stop_rect(self, event):
        self.canvas.create_rectangle(self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y, outline=self.color, width=self.line_width, tags="perm_rect")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
    
    def draw_circle(self):
        self.canvas.bind("<ButtonPress-1>", self.start_circ)
    def start_circ(self,event):
        self.circ_start_x = event.x
        self.circ_start_y = event.y
        self.canvas.bind("<B1-Motion>", self.draw_circ)
        self.canvas.bind("<ButtonRelease-1>", self.stop_circ)

    def draw_circ(self,event):
        self.circ_end_x = event.x
        self.circ_end_y = event.y
        self.canvas.delete("temp_circ")
        self.canvas.create_oval(self.circ_start_x, self.circ_start_y, self.circ_end_x, self.circ_end_y, outline=self.color, width=self.line_width, tags="temp_circ")
    
    def stop_circ(self, event):
        self.canvas.create_oval(self.circ_start_x, self.circ_start_y, self.circ_end_x, self.circ_end_y, outline=self.color, width=self.line_width, tags="perm_circ")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    

root = Tk()
root.title("Painter")
painter = Painter(root)
root.mainloop()
