import cairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# set line color and width
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(20)


# Butt cap
ctx.move_to(100,80)
ctx.line_to(500, 80)
ctx.set_line_cap(cairo.LINE_CAP_BUTT)
ctx.stroke()

# square cap
ctx.move_to(100, 200)
ctx.line_to(500, 200)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.stroke()

# Round Cap
ctx.move_to(100, 320)
ctx.line_to(500, 320)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

file_path = "output/linestyles.png"

surface.write_to_png(file_path)
