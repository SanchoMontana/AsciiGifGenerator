from __future__ import print_function
import splice
import os
from time import sleep
from PIL import Image
from PIL import ImageEnhance
filename = raw_input("Enter the path to gif: ")
density = 3
try:
    pic = Image.open(filename)
except:
    print("File does not exsist :(")
    quit()
everything = []
while 1:
    try:
        pic.seek(pic.tell() + 1)
    except:
        break
    img = pic.convert("LA")
    img = img.resize((img.size[0], int(img.size[1] * 0.7)))
    img = ImageEnhance.Contrast(img)
    img = img.enhance(1)
    pix = img.load()
    avgpix = 0
    allpixarray = []
    for y in range(int(img.size[1]/density)):
        pixarray = []
        for x in range(int(img.size[0]/density)):
            for i in range(density):
                for j in range(density):
                    avgpix += pix[x * density + i,y * density + j][0]
            avgpix = int(avgpix / (density**2))
            pixarray.append(avgpix)
            avgpix = 0
        allpixarray.insert(0, pixarray)
    allpixarray = list(reversed(allpixarray))
    #for i in range(len(allpixarray)):
    #    os.system("printf '\e[A'")
    #    pass
    asciiarray = []
    for i in allpixarray:
        pixarray = []
        for j in i:
            if 0 <= j < 28:
                pixarray.append(" ")
            elif 28 <= j < 56:
                pixarray.append(".")
            elif 56 <= j < 84:
                pixarray.append(",")
            elif 84 <= j < 112:
                pixarray.append(";")
            elif 112 <= j < 140:
                pixarray.append("^")
            elif 140 <= j < 168:
                pixarray.append("=")
            elif 168 <= j < 196:
                pixarray.append("*")
            elif 196 <= j < 224:
                pixarray.append("%")
            elif 224 <= j < 256:
                pixarray.append("@")

	asciiarray.append(pixarray)
    everything.append(asciiarray)

allFrames = []
frameString = ""
rows = len(everything[0])
for frame in everything:
    frameString = ""
    for row in frame:
        for char in row:
            frameString += char
        frameString += "\n"
    allFrames.append(frameString)
cropWidth = 1920 - rows * 13
cropHeight = 1080 - len(everything) * 21
createGif = raw_input("Do you intend to make into a gif? [y/n]: ")

if createGif.lower() == "y" or createGif.lower().startswith("yes"):
    for frame in range(len(allFrames)):
        print(allFrames[frame])
        sleep(0.04)
        os.system("import -window root -crop 1920x1080-" + str(cropWidth) + "-" + str(cropHeight) + " frames/frame" + str(frame) + ".png")
        os.system("clear")
    splice.makeGif()

else:
    while True:
        for frame in range(len(allFrames)):
            print(allFrames[frame])
            print("\n[Ctrl+C] to quit")
            sleep(0.09)
            os.system("clear")
	
