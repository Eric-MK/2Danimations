import cairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color A Cairo context is created to work with the image surface. The context is like a "pen" that you use to draw on the canvas.
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Bezier curve
ctx.move_to(100, 100)
ctx.curve_to(200, 0, 400, 200, 500, 100)
ctx.line_to(500, 300)
ctx.curve_to(400, 400, 200, 200, 100, 300)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()

file_path = "output/polycurves.png"

surface.write_to_png(file_path)