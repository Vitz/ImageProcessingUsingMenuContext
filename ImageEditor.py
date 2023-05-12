from os.path import isfile, isdir
from os import listdir, path
import sys
from PIL import Image


class ImageEditor():
    def quick_resize_max_1280x720(self, item):
        x = (1280, 720)
        try:
            img = Image.open(item)
            width, height = img.size
            if width > x[0] or height > x[1]:
                img.thumbnail(x, Image.ANTIALIAS)
            img.save(item.replace(".jpg", "").replace(".png", "") + "max1280" + ".jpg", subsampling=0, quality=100)
        except Exception as e:
            print(str(e))

    def quick_create_square_dir(self, root):
        all = []
        for sub in listdir(root):
            sub_full = path.join(root, sub)

            if isfile(sub_full):
                all.append(sub_full)

            if isdir(sub_full):
                for only_files in listdir(sub_full):
                    only_files_full = path.join(sub_full, only_files)
                    if isfile(only_files_full):
                        all.append(only_files_full)

        for file in all:
            self.quick_create_square(file, replace=True)

    def quick_create_square(self, item, replace=False):
        try:
            img = Image.open(item)
            width, height = img.size
            margin_size = width - height
            if margin_size > 0:
                result = self.add_margin(img,
                                         top=int(margin_size / 2),
                                         right=0,
                                         bottom=int(margin_size / 2),
                                         left=0,
                                         color="#FFFFFF")
            else:
                result = self.add_margin(img,
                                         top=0,
                                         right=int(-margin_size / 2),
                                         bottom=0,
                                         left=int(-margin_size / 2),
                                         color="#FFFFFF")

            path = item.replace(".jpg", "").replace(".png", "") + ".jpg"
            if not replace:
                path.replace(".jpg", "Sq.jpg")
            result.save(path, subsampling=0, quality=100)
        except Exception as e:
            print(str(e))

    def quick_reduce_10(self, item):
        try:
            img = Image.open(item)
            width, height = img.size

            crop_width = width - int(width / 5)
            crop_height = height - int(height / 5)

            img = img.crop(((width - crop_width) // 2,
                            (height - crop_height) // 2,
                            (width + crop_width) // 2,
                            (height + crop_height) // 2))

            img.save(item.replace(".jpg", "") + "Rd" + ".jpg", subsampling=0, quality=100)

        except Exception as e:
            print(str(e))

    def add_margin(self, img, top, right, bottom, left, color):
        width, height = img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(img.mode, (new_width, new_height), color)
        result.paste(img, (left, top))
        return result
