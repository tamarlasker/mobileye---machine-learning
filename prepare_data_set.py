import random
import glob
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np


def read_dirs(dir):
    cities_dir = r"C:\Users\RENT\Desktop\Mobileye\images\gtFine\{}".format(dir)
    cities = os.listdir(cities_dir)
    lables = []
    imgs = []
    for city in cities:
        print(city)
        labels_dir = rf"C:\Users\RENT\Desktop\Mobileye\images\gtFine\{dir}\{city}\*gtFine_labelIds.png"

        img_dir = rf"C:\Users\RENT\Desktop\Mobileye\images\leftImg8bit\{dir}\{city}\*.png"

        lables += glob.glob(os.path.join(labels_dir))
        imgs += glob.glob(os.path.join(img_dir))

    return imgs, lables

croped_imgs = []
labels = []


 def open_images_files():
     return glob.glob('C:/Users/RENT/Desktop/aachen/**/*.png', recursive=True)


     return glob.glob('C:/Users/RENT/Desktop/labels/**/*ds.png', recursive=True)
 def open_labels_files():


def add_zeroes_to_edge(image_):
    return np.pad(image_, pad_width=41, mode='constant', constant_values=0)


def crop(image, pixel):
    try:
        return image[pixel[0] - 40 : pixel[0] + 41, pixel[1] - 40 : pixel[1] + 41]
    except IndexError:
        return add_zeroes_to_edge(image)


def write_to_files(images, labels):

    np.array(images, dtype='uint8').tofile('data.bin')
    np.array(labels, dtype='uint8').tofile('labels.bin')


def prepare_img(image, pixel, tfl_sign):
    croped_image = crop(image, pixel)
    croped_imgs.append(croped_image)
    labels.append(tfl_sign)
    # plt.imshow(croped_image)
    # plt.show()


def find_tfls_pixels(labeled_name):
    labeled_image = np.asarray(Image.open(labeled_name))
    return random.choice(np.argwhere(labeled_image == 19))


def find_not_tfls_pixels(labeled_image):
    return random.choice(np.argwhere(labeled_image != 19))


def init_data_set():
    images = open_images_files()
    labeled_imgs = open_labels_files()

    for img, label in zip(images, labeled_imgs):
        image = plt.imread(img)
        try:
            tfl_pixels = find_tfls_pixels(label)
        except:
            continue

        prepare_img(image, tfl_pixels, 1)
        prepare_img(image, find_not_tfls_pixels(image), 0)

    write_to_files(croped_imgs, labels)


def get_label(index):
    data = np.fromfile('data.bin')
    # plt.imshow(data[index])
    # plt.show()
    return np.fromfile('labels.bin')[index]

def paste_rectangles(images):
    img = plt.imread('img_for_crop.png')
    rec = img[50:110, 1858:1867]
    for img in images:
        pixel = (random.randint(0, 20), random.randint(0, 71))
        for i in range(60):  # for paste a piece of image on other image.
            for j in range(9):
                img[0][pixel[0] + i][pixel[1] + j] = rec[i][j]


init_data_set()