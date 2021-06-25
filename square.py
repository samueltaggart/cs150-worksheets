import picture

#Creates a blank canvas, 300 pixels high and 300 wide.
picture.new_picture(300, 300)

#We'll be using picture.py's pen to draw our square.
#This sets the stroke width to 8 pixels, and the color to purple.
picture.set_pen_width(8)
picture.set_outline_color("purple")

#Starts the pen's location at 100 pixels down and right from the top left corner.
set_position(100, 100)

#Sets the initial angle to 0 degrees: straight right.
set_direction(0)

#Some code to show you what drawing can look like.
#Delete the stuff below and add code to draw a square.
draw_forward(100)
rotate(30)
draw_forward(75)
rotate(30)
draw_forward(50)
rotate(30)
draw_forward(25)
rotate(30)
draw_forward(12)


#Displays the picture when you're all done drawing. Don't delete.
display()
