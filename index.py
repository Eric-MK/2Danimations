import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
# Fill the Entire Surface with the Set Color
ctx.paint()

# Draw the image rectangle(x,y,width,height) 
ctx.rectangle(150, 100, 100, 240)
# sets the fill color to red.
ctx.set_source_rgb(1,0,0)
#  fills the defined rectangle with the red color, effectively drawing a red rectangle on the canvas.This function looks at the path we have defined and fills it with the color we previously selected
ctx.fill() 

# Green Rectangle
ctx.rectangle(300, 100, 100, 240)
ctx.set_source_rgb(0,1,0)
ctx.fill()

# Blue Square
ctx.rectangle(350, 170, 200, 200)
ctx.set_source_rgb(0,0,1)
ctx.fill()

#save the image in a png file
surface.write_to_png("output.png")
