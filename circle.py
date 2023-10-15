import cairo
import math
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


# small circle
ctx.arc(300,200, 50,0,2*math.pi)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

# medium circle
ctx.arc(300,200,100,0,2*math.pi)
ctx.set_source_rgb(1,0,1)
ctx.set_line_width(10)
ctx.stroke()

# Large Circle
ctx.arc(300, 200, 150, 0, 2*math.pi)
ctx.set_source_rgb(1,1,1)
ctx.set_line_width(10)
ctx.stroke()


file_path = "output/circle.png"

surface.write_to_png(file_path)