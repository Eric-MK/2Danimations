import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)

# relative drawing function
a = 0.523599 # radian equals 30 degree
r = 100
x1 = 300
y1 = 200
ctx.move_to(x1,y1)
# The math.cos(a) and math.sin(a) functions are responsible for converting the angle a into x and y coordinates on the canvas. 
# ctx.line_to(x1 + r*math.cos(a), y1 + r*math.sin(a))

# to draw a line segment relative to the current point (the starting point).
ctx.rel_line_to(r*math.cos(a),r*math.sin(a))
ctx.stroke()

file_path = "output/lineangle2.png"

surface.write_to_png(file_path)