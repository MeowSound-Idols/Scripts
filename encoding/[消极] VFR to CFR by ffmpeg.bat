@echo off
echo Converting Video
"ffmpeg.exe" -y -i "%~1" -an -pix_fmt yuv420p -f yuv4mpegpipe - | "NVEncC64.exe" --y4m -i - -o "%~1.x264" 
echo Copying Audio
"ffmpeg.exe" -i "%~1" -vn -sn -c:a copy -y -map 0:a:0 "%~1.aac"
echo Muxing
"mkvmerge.exe" -o "%~d1%~p1%~n1.cfr.mkv" "%~1.x264" "%~1.aac"
echo Deleting Files
del "%~1.x264"
del "%~1.aac"
pause
