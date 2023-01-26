from PIL import Image
import os
import time
import sys

totalAssets = 0
totalFailures = []

try:
    indir = sys.argv[0]
except IndexError:
    print("No input dir has been specified.\nWhere would you like these files to come from? (required)")
    indir = input()

try:
    outdir = sys.argv[1]
except IndexError:
    print("No output dir has been specified.\nWhere would you like these files to go? "
          "(type \"none\" to replace all files: THIS WILL ERASE EVERY ASSET)")
    answer = input()
    if answer == "none":
        outdir = indir
    else:
        outdir = input() + '/'


startTime = time.time()


def process(_filename):
    global totalAssets
    global outdir

    image = Image.open(_filename)
    output = Image.new("RGBA", (image.width * 2, image.height * 2))

    for i in range(2):
        for j in range(2):
            output.paste(image, (i * image.width, j * image.height))

    directory = os.path.dirname(outdir + _filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    output.save(outdir + _filename)

    totalAssets += 1


def run():
    for asset in os.listdir(indir + 'assets/minecraft/textures/block'):
        name, extension = os.path.splitext(asset)
        if extension == ".png":
            try:
                process(indir + 'minecraft/textures/block/' + asset)
            except:
                print("failed on", asset)
                totalFailures.append(asset)
        else:
            pass


run()
endTime = time.time()
print(totalAssets, "assets processed in", round(endTime - startTime, 4), "seconds")
