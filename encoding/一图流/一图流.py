import os
import sys
from subprocess import call
# change cwd
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
if len(sys.argv) != 3:
    print('Missing arguments')
    exit()

if sys.argv[1].endswith(('png', 'jpg', 'jpeg', 'webp', 'gif')):
    image_path = sys.argv[1]
    audio_path = sys.argv[2]
else:
    image_path = sys.argv[2]
    audio_path = sys.argv[1]
# call scg
print('生成图片')
call('./scg_v0.0.1/static-cover-generator.exe -i "{}" -o "{}"'.format(image_path, image_path + '.output.png'))
# call ffmpeg
print('开始压制')
# ↓ 修改到你的 ffmpeg 路径
call('E:/Temp/ffmpeg.exe -loop 1 -r 24 -i "{}" -i "{}" -bsf:a aac_adtstoasc -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -b:a 320k -shortest -pix_fmt yuv420p "{}"'.format(image_path + '.output.png', audio_path, audio_path + '.scg.mp4'))
print('删除中间文件')
os.remove(image_path + '.output.png')