@echo off

if not "%2"=="" (
    echo Error! You may only pass one argument
    exit 1
)

set name=day%1

cargo new --bin %name%
mkdir %cd%\%name%\input
echo.> %cd%\%name%\input\input.txt