import sys

from PIL import Image

class ImageEditor():
    def __init__(self):
        pass

    def create_squere(self, item):
        try:
            print("q")
            img = Image.open(item)
            width, height = img.size
            margin_size = width - height
            if margin_size > 0:
                result = self.add_margin(img, top=int(margin_size/2), right=0, bottom=int(margin_size/2), left=0, color= "#FFFFFF")
            else:
                result = self.add_margin(img, top=0, right=int(margin_size/2), bottom=0, left=int(margin_size/2), color= "#FFFFFF")
            result.save(item.replace(".jpg", "") + "Sq" + ".jpg")

        except Exception as e:
            print(str(e))
            pass

    def add_margin(self, img, top, right, bottom, left, color):
        width, height = img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(img.mode, (new_width, new_height), color)
        result.paste(img, (left, top))
        return result


if __name__ == '__main__':
    ie = ImageEditor()
    for idx,item in enumerate(sys.argv):
        if idx == 0:
            continue
        ie.create_squere(item)



