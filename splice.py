import imageio
import os

def makeGif():
    images = []
    frames = os.listdir("frames/")
    frameDuration = 1 / float(raw_input("Input desired frame rate:\n>>> "))
    print "Crafting gif..."
    for i in range(len(frames)):
        images.append(imageio.imread("frames/frame" + str(i) + ".png"))
    imageio.mimsave("result.gif", images, format='GIF', duration=frameDuration)
    print "gif completed successfully :)"
    view = raw_input("View gif now? [y/n]: ")
    if view.lower() == "y" or view.lower().startswith("yes"):
        os.system("animate result.gif &")
if __name__ == "__main__":
    makeGif()
