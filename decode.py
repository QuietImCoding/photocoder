from PIL import Image
import math

path = raw_input("Pick a file: ")

im = Image.open(path)
width = im.size[0]
height = im.size[1]
pix = im.load()
print "Width: " + str(im.size[0]) + ", Height: " + str(im.size[1])
oy = height/2.0
ox = width/2.0
mdist = int(math.sqrt(((oy)**2 + (ox)**2)))
numlist = []
for x in range(0, width):
    dist = int(math.sqrt(((oy)**2 + (ox-x)**2)))
    normdist = int(255 * dist / mdist)
    r = pix[x, 0][0]
    number = r - 255 + normdist
    numlist.append(number)

for y in range(0, height):
    dist = int(math.sqrt(((oy-y)**2 + (ox)**2)))
    normdist = int(255 * dist / mdist)
    g = pix[0, y][1]
    number = g - 255 + normdist
    numlist[y] = int(round((numlist[y] + number) / 2))

mystery = ""
for i in numlist:
    mystery += chr(i)
print mystery
