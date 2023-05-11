import sys
from ImageEditor import ImageEditor

if __name__ == '__main__':
    ie = ImageEditor()
    print(sys.argv)
    print(sys.argv[1])

    run = getattr(ImageEditor, sys.argv[1].replace("--", ""))
    run(ie, sys.argv[2])

