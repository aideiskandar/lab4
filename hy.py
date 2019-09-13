from sense_hat import SenseHat
sense = SenseHat()

def textcolor():
    while True: #infinite loop cos always true
        text_colour = int(input("Choose colour of text: 1-red, 2-green, 3-blue"))
        if text_colour == 1:
            print("You have chosen red colour for your message.")
            rgb = (255,0,0)
            break #break out of loop the moment we get a value
        elif text_colour == 2:
            print ("You have chosen green colour for your message.")
            rgb = (0,255,0)
            break
        elif text_colour == 3:
            print("You have chosen blue colour for your message.")
            rgb = (0,0,255)
            break
    bgcolor(rgb) #throws rgb variable into next method/loop

def bgcolor(rgb): #same idea as msg colour
    ##text_colour = int(input("Choose colour of text: 1-red, 2-green, 3-blue")) remove cos you want it in a loop
    while True:
        text_colour = int(input("Choose colour of background: 1-red, 2-green, 3-blue"))
        if text_colour == 1:
            print("You have chosen red colour for your background.")
            bg_colour = (255,0,0)
            break
        elif text_colour == 2:
            print ("You have chosen green colour for your background.")
            bg_colour = (0,255,0)
            break
        elif text_colour == 3:
            print("You have chosen blue colour for your background.")
            bg_colour = (0,0,255)
            break
    sameColour(rgb,bg_colour)
    
def sameColour(rgb, bg_colour):
    if rgb == bg_colour:
        print("You have chosen the same colour for both message and background. Please change colours.")
        bgcolor(rgb)
    else:
        display(rgb,bg_colour)  #now we are throwing in 2 variables into the next method/loop so that the variables are not destroyed

def display(rgb, bg_colour):
    sense.set_rotation(0)
    speed = float(input("Enter desired speed ranging from 0.01 as fastest to 1 as slowest"))
    sense.show_message (message, text_colour= rgb, back_colour= bg_colour, scroll_speed= speed)
    sense.clear(199,199,199)

message= input("Enter your message here")
textcolor()