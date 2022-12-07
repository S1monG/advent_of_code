@echo off

set name=day%1

cargo new --bin %name%
mkdir %cd%\%name%\input
echo.> %cd%\%name%\input\input.txt