from PIL import Image
import os
import time
import sys

totalAssets = 0
totalFailures = []

try:
    outfile = sys.argv[1]
except IndexError:
    print("No output dir has been specified.\nWhere would you like these files to go?")
    answer = input()
    if answer == "none":
        outfile = ""
    else:
        outfile = input() + '/'


startTime = time.time()


def process(_filename):
    global totalAssets
    global outfile

    image = Image.open(_filename)
    output = Image.new("RGBA", (image.width * 2, image.height * 2))

    for i in range(2):
        for j in range(2):
            output.paste(image, (i * image.width, j * image.height))

    directory = os.path.dirname(outfile + _filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    output.save(outfile + _filename)

    totalAssets += 1


def run():
    for asset in os.listdir('assets/minecraft/textures/block'):
        name, extension = os.path.splitext(asset)
        if extension == ".png":
            try:
                process('minecraft/textures/block/' + asset)
            except:
                print("failed on", asset)
                totalFailures.append(asset)
        else:
            pass


run()
endTime = time.time()
print(totalAssets, "assets processed in", round(endTime - startTime, 4), "seconds")
