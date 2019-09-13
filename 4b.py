from sense_hat import SenseHat
sense = SenseHat()

textcolor = []
bgcolor = []
scroll = 0.0
compare = lambda x,y: x == y

def colorinput():
    while True:
        try:
            textcolor.append(int(input("Enter Text RGB Value")))
            if len(textcolor) >= 3:
                break
        except ValueError:
            print("Please enter whole number")
    bgcolorinput()
            
def bgcolorinput():
    while True:
        try:
            bgcolor.append(int(input("Enter Background RGB Value")))
            if len(bgcolor) >= 3:
                break
        except ValueError:
            print("Please enter whole number")
    scrollspeed()
            
def scrollspeed():
    scroll = 0.0
    while True:
        try:
            value = float(input("Enter Scroll Speed Value (0.1 ~ 0.9)"))
            if value != 0.0:
                break
        except ValueError:
            print("Please enter decimal number")
    display(value)

def display(value):
    scroll = value
    cleandata = list(map(lambda x: 255 if x > 255 else (0 if x < 0 else x), textcolor))
    del textcolor[:]
    textcolor.extend(cleandata)
    cleandata1 = list(map(lambda x: 255 if x > 255 else (0 if x < 0 else x), bgcolor))
    del bgcolor[:]
    bgcolor.extend(cleandata1)

    if compare(textcolor,bgcolor) == False:
        sense.show_message("Hello", text_colour = textcolor, back_colour  = bgcolor, scroll_speed = scroll)
        restart()
    else:
        print("Both Colors are the same, Please redo all inputs")
        clearval()
        colorinput()

def restart():
    res = input("Do you still want to continue ?").lower()
    if res == 'y':
        clearval()
        colorinput()

def clearval():
        del textcolor[:]
        del bgcolor[:]

colorinput()