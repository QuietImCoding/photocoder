import math

f = open("leedle.ppm", "w")

text = raw_input("What to encode: ")
width = len(text)#720
height = len(text)#720

f.write("P3 %s %s 255\n" % (width, height))

bigstr = ""

oy = height/2.0
ox = width/2.0
mdist = int(math.sqrt(((oy)**2 + (ox)**2)))
numstr = ""
for y in range(0, height):
    for x in range(0, width):
        dist = int(math.sqrt(((oy-y)**2 + (ox-x)**2)))
        normdist = int(255 * dist / mdist)
        r = 255 - (normdist - ord(text[x]))
        if y == 0:
            numstr += str(ord(text[x])) + " "
        g = 255 - (normdist - ord(text[y]))
        b = 255 - normdist
        bigstr += "%s %s %s\n" % (r, g, b)

bigstr = bigstr[:len(bigstr)-2]

f.write(bigstr)
    
