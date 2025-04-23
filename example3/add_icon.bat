@echo off
set EXE=app.exe
set OUT=my_app_with_icon.exe
set ICO=main.ico
set RC=app_icon.rc
set RES=app_icon.res
set RH="C:\Program Files (x86)\Resource Hacker\ResourceHacker.exe"

set COMPANY_NAME=Your Company
set FILE_DESCRIPTION=My Application
set FILE_VERSION=1.0.0.0
set PRODUCT_NAME=MyApp
set PRODUCT_VERSION=1.0.0.0
set LEGAL_COPYRIGHT=© 2025 Your Company

:: === 生成 .rc 文件 ===
(
@rem echo #include ^<winver.h^>
echo MAINICON ICON "%ICO%"
echo 1 VERSIONINFO
echo FILEVERSION %FILE_VERSION:.=,%
echo PRODUCTVERSION %PRODUCT_VERSION:.=,%
echo BEGIN
echo     BLOCK "StringFileInfo"
echo     BEGIN
echo         BLOCK "040904E4"
echo         BEGIN
echo             VALUE "CompanyName", "%COMPANY_NAME%"
echo             VALUE "FileDescription", "%FILE_DESCRIPTION%"
echo             VALUE "FileVersion", "%FILE_VERSION%"
echo             VALUE "ProductName", "%PRODUCT_NAME%"
echo             VALUE "ProductVersion", "%PRODUCT_VERSION%"
echo             VALUE "LegalCopyright", "%LEGAL_COPYRIGHT%"
echo         END
echo     END
echo     BLOCK "VarFileInfo"
echo     BEGIN
echo         VALUE "Translation", 0x409, 1252
echo     END
echo END
) > %RC%
%RH% -open %RC% -save %RES% -action compile
%RH% -open %EXE% -save %OUT% -action addoverwrite -res %RES%

echo Done! Output: %OUT%
pause