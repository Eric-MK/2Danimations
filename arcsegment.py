import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_line_width(10)
ctx.set_source_rgb(0,0,0.5)

# Arc
ctx.arc(200,200, 150, 3*math.pi/4, 5*math.pi/4)

# segment
ctx.new_sub_path()
ctx.arc(350, 200, 150, 3*math.pi/4, 5*math.pi/4)
ctx.close_path()

# sector
ctx.move_to(500, 200)
ctx.arc(500, 200, 150, 3*math.pi/4, 5*math.pi/4)
ctx.close_path()

ctx.stroke()

file_path = "output/arcs.png"

surface.write_to_png(file_path)