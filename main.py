#######################################################################################################
########## IMPORT
#######################################################################################################

from tkinter import *
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

#######################################################################################################
########## FUNCTION
#######################################################################################################


def greeting():
    try:
        print("\n\n\nWelcome the the drawing program ! When the window will appears, type m to start drawing, type f to stop"
            "\nRemember to end where you started drawing\n")
        red_coef = float(input("Choose the reduction coefficient (float):\n"))
    except ValueError as e:
        print(f"You can only write floats error = '{e}'")
        greeting()


def get_mouse_input(event):
    # get mouse coordinates on the screen
    x, y = event.x, event.y
    logging.debug(f"Mouse input:{x=};{y=}")
    if mouse:
        logging.debug("in mouse true")
        draw_path(x, y)


def draw_path(x, y):
    global path
    global x_max
    global y_max
    # draw the path on the screen
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
    logging.debug(f"x_max= {x_max}")
    logging.debug(f"y_max={y_max}")
    logging.info(f"path.lenght = {len(path)}")
    if key == "m":
        # get mouse input
        mouse = True
        logging.debug("mouse true")
    elif key == "f":
        mouse = False
        with open("listcoord.js", "w") as list:
            list.write("let drawing_2 = [\n")
            for line in path:
                x, y = line
                # transform the coordinates to have negative values
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

# size of the screen
Width = 1900
Height = 920

# initialization of the variables
path = []
count = 0
mouse = False
red_coef = 1
x_max = y_max = 0

# ask the user to choose the reduction coefficient
greeting()

# create the first window
window = Tk()

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

# add texts to the frame
canvas.pack(expand=YES)

#look for input
window.bind("<Key>", key_pressed)
window.bind("<Motion>", get_mouse_input)

# display
window.mainloop()
