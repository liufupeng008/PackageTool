#!/usr/bin/env python3
import os
import numpy
import argparse
from PIL import Image


def get_filename_extension(fp):
    '''
    Get filename extension.
    :param fp: A file path (string)
    :return: filename extension
    '''
    filename_extension = os.path.splitext(fp)[1]
    return filename_extension


def get_image_mode(fp):
    '''
    Get image mode.
    :param fp: A file path (string)
    :return: image mode
    '''
    try:
        img = Image.open(fp)
        return img.mode
    except:
        return None


def is_there_alpha_channel(fp):
    '''
    Determine if the PNG image has an alpha channel.
    :param fp: A PNG file path (string)
    :return: is there alpha channel
    '''
    if get_image_mode(fp) == 'RGBA':

        try:
            img = Image.open(fp)
        except:
            return False

        alpha = img.split()[3]
        arr = numpy.asarray(alpha)
        count = 0
        for i in range(0, img.size[0] - 1):
            for j in range(0, img.size[1] - 1):
                if arr[j][i] < 128:
                    count += 1
                    if count > 10:
                        break
        if count > 10:
            return True
        else:
            return False
    else:
        return False


def remove_image_alpha_channel(src, dst):
    '''
    Remove image alpha channel.
    :param src: source image
    :param dst: destination image
    :return: None
    '''
    try:
        im = Image.open(src)
        x, y = im.size
        im_temp = Image.new('RGBA', im.size, (255, 255, 255))
        im_temp.paste(im, (0, 0, x, y), im)
        im_new = im_temp.convert('RGB')
        im_new.save(dst)
        print('Remove alpha channel succeed.')
    except:
        print('Remove alpha channel failed.')


def main(src, dst, is_force):
    '''
    Remove image alpha channel.
    :param src: source image
    :param dst: destination image
    :param is_force: is remove alpha channel by force
    :return: None
    '''
    if get_filename_extension(src) == '.png' or get_filename_extension(src) == '.PNG':
        if is_force:
            remove_image_alpha_channel(src, dst)
        else:
            if is_there_alpha_channel(src):
                remove_image_alpha_channel(src, dst)
            else:
                print('The src file does not have alpha channel.')
    else:
        print("The src filename extension is not 'PNG'.")



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str, help="the source PNG file")
    parser.add_argument("dst", type=str, help="the destination PNG file")
    parser.add_argument("-f", "--force", action="store_true", help="remove alpha channel by force")
    args = parser.parse_args()

    main(args.src, args.dst, args.force)