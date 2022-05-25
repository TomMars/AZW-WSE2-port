@echo off
python process_shaders.py
@del *.pyc
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul