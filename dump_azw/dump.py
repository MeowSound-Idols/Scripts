# Special Thanks: https://fireattack.wordpress.com/2018/05/16/automating-kindle-ebook-image-extraction/
# Requirements
# 1. Modified DumpAZW6_v1.py
# 1.5 Python 2.7
# 2. Modified DeDRM Plugin for Calibre
# 3. Calibre
import os
import glob as gb
import sys
from shutil import copyfile, rmtree
from subprocess import call
# change cwd
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

if len(sys.argv) != 3:
    print('Missing arguments')
    exit()

PYTHON_27_PATH = 'D:/Python27/python.exe'
DUMP_AZW6_SCRIPT_LOCATION = './DumpAZW6_v01.py'
CALIBRE_CLI_PATH = 'C:/Program Files (x86)/Calibre2/ebook-convert.exe'

if sys.argv[1].endswith('.res'):
    resource_path = sys.argv[1]
    book_path = sys.argv[2]
else:
    resource_path = sys.argv[2]
    book_path = sys.argv[1]

# dump resource file
call('"{}" "{}" "{}" "{}"'.format(PYTHON_27_PATH, DUMP_AZW6_SCRIPT_LOCATION, resource_path, os.path.dirname(resource_path)))

# 使用以下两行的方式直接调用，取代建立一个新进程
# from DumpAZW6_v01 import main
# main(['DumpAZW6_v01.py', resource_path, os.path.dirname(resource_path)])


# convert azw to zip by calibre
call('"{}" "{}" temp.zip --extract-to "{}"'.format(CALIBRE_CLI_PATH, book_path, os.path.dirname(book_path) + '/book_files'))
output_image_path = os.path.dirname(book_path) + '/book_files/temp_files/images'
hd_images_path = os.path.dirname(resource_path) + '/azw6_images'
# check if images have a HD versions
images = gb.glob(output_image_path + '/*.jpeg')
for image in images:
    filename = os.path.basename(image)
    if os.path.exists(hd_images_path + '/HDimage' + filename):
        # copy hd image
        print('Copy {} -> {}'.format(hd_images_path + '/HDimage' + filename, output_image_path + '/' + filename))
        copyfile(hd_images_path + '/HDimage' + filename, output_image_path + '/' + filename)

# clean temporary files
os.remove('./temp.zip')
# rmtree(os.path.dirname(book_path) + '/book_files')
rmtree(os.path.dirname(resource_path) + '/azw6_images')