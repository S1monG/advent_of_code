@echo off

if not "%2"=="" (
    echo Error! You may only pass one argument
    exit 1
)

set name=day%1

mkdir %cd%\%name%\src
echo import os> %cd%\%name%\src\main.py
echo from pathlib import Path>> %cd%\%name%\src\main.py
echo.>> %cd%\%name%\src\main.py
echo parent_dir = Path(os.path.dirname(__file__)).parent>> %cd%\%name%\src\main.py
echo abs_file_path = os.path.join(parent_dir, 'data/input.txt')>> %cd%\%name%\src\main.py
echo.>> %cd%\%name%\src\main.py
echo with open(abs_file_path) as file:>> %cd%\%name%\src\main.py
echo     pass>> %cd%\%name%\src\main.py

mkdir %cd%\%name%\data
echo.> %cd%\%name%\data\input.txt