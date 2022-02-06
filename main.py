#######################################################################################################
########## IMPORT
#######################################################################################################
from tkinter import *
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
#######################################################################################################
########## FUNCTION
#######################################################################################################


def get_mouse_input(event):
    x, y = event.x, event.y
    logging.debug(f"Mouse input:{x=};{y=}")
    if mouse:
        logging.debug("in mouse true")
        draw_path(x, y)


def draw_path(x, y):
    global path
    global x_max
    global y_max
    logging.debug("draw")
    img.put("#000000", (x, y))
    path.append((x, y))
    x_max = max([x, x_max])
    y_max = max([y, y_max])


def key_pressed(event):
    key = event.char
    global count
    global path
    global mouse
    logging.error(f"x_max= {x_max}")
    logging.error(f"y_max={y_max}")
    logging.error(f"path.lenght = {len(path)}")
    if key == "m":
        # get mouse input
        mouse = True
        logging.error("mouse true")
    elif key == "f":
        mouse = False
        with open("listcoord.js", "w") as list:
            list.write("let drawing_2 = [\n")
            for line in path:
                x, y = line
                # transform the coordinates from a (0;x),(0;y) matrix to a (-x/2;x/2),(-y/2;y/2) matrix
                x = x / red_coef
                if x <= (x_max / red_coef):
                    x = x - (x_max / red_coef)
                y = y / red_coef
                if y <= (y_max / red_coef):
                    y = y - (y_max / red_coef)
                line = "{ x:"+str(x), "y:"+str(y)+"},"
                list.write(str(line).replace("'", '').replace("(", "").replace(")", "")+'\n')
            list.write("];")


#######################################################################################################
########## SCRIPT
#######################################################################################################


# background colors
gray = "#717C7A"
white = "#FFFFFF"
blue_green = "#2CDF85"
background_color = gray
Width = 1900
Height = 920
path = []
count = 0
mouse = False
red_coef = 1
x_max = y_max = 0

red_coef = float(input("Choose the reduction coeficient (float):\n"))

# create the first window
window = Tk()

#create the frame
#frame = Frame(window, bg=gray)

# Create the canva and the image to draw the path on
canvas = Canvas(window, width=Width, height=Height, bg=gray)
canvas.pack()
img = PhotoImage(width=Width, height=Height)
canvas.create_image((Width/2, Height/2), image=img, state="normal")

# customize the window
window.title("Design It")
window.geometry("1080x720")
window.minsize(Width, Height)
window.iconbitmap("icon.ico")
window.config(background=background_color)

# add some text
# random_title = Label(canvas, text="random text", font=("Arial", 40), bg=gray, fg=white)
# random_title.pack()

# add texts to the frame
canvas.pack(expand=YES)

# add button
# pen_button = Button(canvas, text="image", font=("Arial", 40), bg=gray, fg=white) #command=
# pen_button.pack(pady=25, fill=X)

#look for input
window.bind("<Key>", key_pressed)
window.bind("<Motion>", get_mouse_input)

# display
window.mainloop()