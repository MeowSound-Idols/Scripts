## 运行本脚本你需要

1. 修改过的`DumpAZW6_v1.py`（随本脚本附赠）
2. Calibre，并安装修改版的 DeDRM 插件（随后说明）
3. Python27

## 使用方法

将`.azw`文件和`.azw.res`文件一起拖动到`dump.bat`上。

## DeDRM 修改方法

解压，打开`__init__.py`，修改125行，在其后增加一行`on_preprocess           = True`。

打包放回。打开`Calibre`加载插件。