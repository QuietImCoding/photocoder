from PIL import Image
import math

path = raw_input("Pick a file: ")

im = Image.open(path)
width = im.size[0]
height = im.size[1]
pix = im.load()
#print "Width: " + str(im.size[0]) + ", Height: " + str(im.size[1])
oy = height/2.0
ox = width/2.0

def decode(big=False):
    mdist = int(math.sqrt(((oy)**2 + (ox)**2)))
    numlist = []
    if big:
        for i in range(1, int(width * height)-1):
            x = int(i % width)
            y = int(i / height)
            dist = int(math.sqrt(((oy-y)**2 + (ox-x)**2)))
            normdist = int(255 * dist / mdist)
            r = pix[x, y][0]
            num = r - 255 + normdist
            if num >= 0 and num <= 255:
                numlist.append(num)
            if r == 0:
                if pix[x, y][1] == 1 and pix[x,y][2] == 2:
                    return numlist
    else:
        for x in range(0, width):
                dist = int(math.sqrt(((oy)**2 + (ox-x)**2)))
                normdist = int(255 * dist / mdist)
                r = pix[x, 0][0]
                number = r - 255 + normdist
                if number > 255 or number < 0:
                    number = 255
                numlist.append(number)
        return numlist

if pix[0,0] == (0, 1, 2):
    print "BIG"
    numlist = decode(True)
else:
    print pix[0,0]
    numlist = decode()
    
mystery = ""
for i in numlist:
    mystery += chr(i)
print mystery
