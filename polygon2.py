import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
# Fill the Entire Surface with the Set Color
ctx.paint()

ctx.move_to(50,100) # A
ctx.line_to(200,50) # B
ctx.line_to(250, 300)  # c
ctx.line_to(100,200)  # D
# completes the closed shape. It adds a line from the current point D back to the first point in the path, which is A.
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("polygon4.png")
