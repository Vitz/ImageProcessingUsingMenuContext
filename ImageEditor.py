import sys
from PIL import Image

class ImageEditor():
    def create_square(self, item):
        try:
            print("q")
            img = Image.open(item)
            width, height = img.size
            margin_size = width - height
            if margin_size > 0:
                result = self.add_margin(img,
                                         top=int(margin_size/2),
                                         right=0,
                                         bottom=int(margin_size/2),
                                         left=0,
                                         color= "#FFFFFF")
            else:
                result = self.add_margin(img,
                                         top=0,
                                         right=int(-margin_size/2),
                                         bottom=0,
                                         left=int(-margin_size/2),
                                         color= "#FFFFFF")
            result.save(item.replace(".jpg", "").replace(".png","") + "Sq" + ".jpg")

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


    def reduce(self, item):
        try:
            print("q")
            img = Image.open(item)
            width, height = img.size

            crop_width = width - int(width / 5)
            crop_height = height - int(height / 5)

            img = img.crop(((width - crop_width) // 2,
                         (height - crop_height) // 2,
                         (width + crop_width) // 2,
                         (height + crop_height) // 2))

            img.save(item.replace(".jpg", "") + "Rd" + ".jpg")

        except Exception as e:
            print(str(e))
            pass

if __name__ == '__main__':
    ie = ImageEditor()

    if(sys.argv[1] ==  "-s"):
        ie.create_square(sys.argv[2])

    if(sys.argv[1] ==  "-r"):
        ie.reduce(sys.argv[2])



