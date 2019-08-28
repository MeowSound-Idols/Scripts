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
# AVS Template
avs_template = r"""
audio = DirectShowSource("{}")
video = ImageSource("{}", fps=30, start=1, end=ceil(30*AudioLengthF(audio)/AudioRate(audio)))
return video
""".format(audio_path, image_path + '.output.png')
f = open(image_path + '.temp.avs', 'wb')
f.write(avs_template.encode('gbk'))
f.close()
# call ffmpeg
print('开始压制')
# ↓ 修改到你的 ffmpeg 路径
call('D:/Downloads/Compressed/NVEnc_4.46/NVEncC/x86/NVEncC.exe -i "{}" -o "{}"'.format(image_path + '.temp.avs', audio_path + '.scg.mp4'))
print('开始混流')
call('E:/Temp/ffmpeg.exe -i "{}" -i "{}" -c:v copy -c:a aac -b:a 320k "{}"'.format(audio_path + '.scg.mp4', audio_path, audio_path + '.scg.mux.mp4'))
print('删除中间文件')
os.remove(image_path + '.output.png')
os.remove(image_path + '.temp.avs')
os.remove(audio_path + '.scg.mp4')