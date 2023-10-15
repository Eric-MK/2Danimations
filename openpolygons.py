import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
# Fill the Entire Surface with the Set Color
ctx.paint()

ctx.move_to(50, 200)
ctx.line_to(100, 200)
ctx.line_to(150,250)
ctx.line_to(250,150)
ctx.line_to(350,250)
ctx.line_to(450,150)
ctx.line_to(500, 200)
ctx.line_to(550, 200)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()


file_path = "output/openpolygon.png"

surface.write_to_png(file_path)


