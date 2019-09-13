from sense_hat import SenseHat
sense = SenseHat()

scrollspeed = float(input("Enter Scroll Speed 0.1 ~ 0.9"))
textcolor = input("Enter RGB values: ")

textcolor = lambda x: 255 if x > 256 else (0 if x < 0 else x),textcolor

print(textcolor)
bcolor = textcolor.split(",")
color = [int(bcolor[0]), int(bcolor[1]), int(bcolor[2])]
sense.show_message("Hello",text_colour = color, scroll_speed = scrollspeed) 