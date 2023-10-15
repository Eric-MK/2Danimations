import cairo
import math
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Bezier curve
ctx.move_to(100, 200)
ctx.curve_to(200, 100, 400, 300, 500, 200)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()



file_path = "output/Beziercurve.png"

surface.write_to_png(file_path)