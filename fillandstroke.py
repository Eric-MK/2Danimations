import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
# Fill the Entire Surface with the Set Color
ctx.paint()

# Fill 
ctx.rectangle(100, 100, 100, 240)
ctx.set_source_rgb(1,0,0)
ctx.fill() 

# Stroke draw the outline of the path with the current source color and line width. It creates the shape of the path's outline.
ctx.rectangle(250, 100, 100, 240)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(5)
ctx.stroke()

# Fill and stroke
ctx.rectangle(400, 100, 100, 240)
ctx.set_source_rgb(0,0,1)
# The fill_preserve operation is similar to fill, but it doesn't clear the path after filling it. This means you can perform additional operations on the same path after filling it. This is particularly useful if you want to both fill and stroke the same path.
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()


#save the image in a png file
surface.write_to_png("outputfillstroke.png")
