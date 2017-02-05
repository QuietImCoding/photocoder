from PIL import Image
import math

read = raw_input("File to encode: ")
rf = open(read, "r")
text = rf.read()
rf.close()


def smallencode(text):
    width = len(text)
    height = len(text)
    f = open("raw.ppm", "w")
    f.write('P3 %s %s 255\n' % (width, height))

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
            #if y == 0:
            #    numstr += str(ord(text[x])) + " "
            g = 255 - (normdist - ord(text[y]))
            b = max(r, g)
            bigstr += '%s %s %s\n' % (r, g, b)

    f.write(bigstr)
    f.close()

def bigencode(text):
    size = math.ceil(math.sqrt(len(text)))
    width = size
    height = size
    f = open("raw.ppm", "w")
    f.write('P3 %s %s 255\n' % (int(width), int(height)))

    bigstr = ""
    
    oy = height/2.0
    ox = width/2.0
    mdist = int(math.sqrt(((oy)**2 + (ox)**2)))
    numstr = ""
    bigstr += '0 1 2\n'
    for i in range(1, int(size**2)-1):
        x = int(i % width)
        y = int(i / height)
        dist = int(math.sqrt(((oy-y)**2 + (ox-x)**2)))
        normdist = int(255 * dist / mdist)
        if i < len(text):
            r = 255 - (normdist - ord(text[i]))
            g = 255 - (normdist - ord(text[x]))
            b = max(r, g)
        else:
            r = 0
            g = 1
            b = 2
        bigstr += '%s %s %s\n' % (r, g, b)

    f.write(bigstr)
    f.close()

if len(text) < 2500:
    smallencode(text)
else:
    bigencode(text)
