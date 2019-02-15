import os, sys, shutil
from subprocess import call
# change cwd
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

if len(sys.argv) == 1:
    print('Missing arguments')
    exit()

call(['sigal', 'build', '-c', './sigal.conf.py', sys.argv[1], sys.argv[1] + '_gallery'])

# 后处理
os.chdir(sys.argv[1] + '_gallery/')
os.mkdir('original')
os.system('move /-y ./*.jpg ./original/')
os.system('move /-y ./*.jpeg ./original/')
os.system('move /-y ./*.png ./original/')
os.system('move /-y ./*.webp ./original/')

with open('./index.html', 'r', encoding='utf-8') as fin:
    with open('./_index.html', 'w', encoding='utf-8') as fout:
        for line in fin.readlines():
            fout.write(line.replace('image: "', 'image: "original/'))
        fin.close()
        fout.close()

os.remove('index.html')