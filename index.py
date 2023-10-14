import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) #create an image surface (PNG) of size 600, 400
# Create a Context and Set the Fill Color
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
# Fill the Entire Surface with the Set Color
ctx.paint()