@echo off
REM ROSSI 46 Chatbot Deployment Script for Windows
REM Automated deployment for public access

echo 🚀 ROSSI 46 CHATBOT DEPLOYMENT WIZARD
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed!
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python found!
echo.

REM Check if required files exist
set "files_missing=0"
for %%f in (chatbot_web.html index.html README_WEB.md server.py) do (
    if not exist "%%f" (
        echo ❌ Missing file: %%f
        set "files_missing=1"
    )
)

if %files_missing% equ 1 (
    echo.
    echo Please make sure all required files are in the current directory.
    echo.
    pause
    exit /b 1
)

echo ✅ All required files found!
echo.

REM Show menu
echo Choose deployment option:
echo.
echo 1. 🚀 Start Local Server (for testing)
echo 2. 📦 Create Deployment Package
echo 3. 🌍 Show Hosting Options
echo 4. 🔍 Show SEO Tips
echo 5. 📋 Show All Options
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto start_server
if "%choice%"=="2" goto create_package
if "%choice%"=="3" goto show_hosting
if "%choice%"=="4" goto show_seo
if "%choice%"=="5" goto show_all
goto invalid_choice

:start_server
echo.
echo 🚀 Starting local server...
echo ==================================================
python server.py
goto end

:create_package
echo.
echo 📦 Creating deployment package...
echo ==================================================
python deploy.py
goto end

:show_hosting
echo.
echo 🌍 HOSTING OPTIONS FOR PUBLIC ACCESS:
echo ==================================================
type DEPLOYMENT_GUIDE.md | findstr /C:"HOSTING OPTIONS" /C:"A) GitHub Pages" /C:"B) Netlify" /C:"C) Vercel" /C:"D) Firebase"
echo.
echo For complete guide, read DEPLOYMENT_GUIDE.md
goto end

:show_seo
echo.
echo 🔍 SEO TIPS FOR BETTER SEARCH VISIBILITY:
echo ==================================================
type DEPLOYMENT_GUIDE.md | findstr /C:"SEO TIPS" /C:"Search Terms People Will Use"
echo.
echo For complete guide, read DEPLOYMENT_GUIDE.md
goto end

:show_all
echo.
echo 🚀 Starting local server...
python server.py
timeout /t 3 /nobreak >nul
echo.
echo 📦 Creating deployment package...
python deploy.py
echo.
echo 🌍 HOSTING OPTIONS:
type DEPLOYMENT_GUIDE.md | findstr /C:"HOSTING OPTIONS" /C:"A) GitHub Pages" /C:"B) Netlify" /C:"C) Vercel" /C:"D) Firebase"
echo.
echo 🔍 SEO TIPS:
type DEPLOYMENT_GUIDE.md | findstr /C:"SEO TIPS" /C:"Search Terms People Will Use"
goto end

:invalid_choice
echo ❌ Invalid choice! Please select 1-5.
echo.

:end
echo.
echo ==================================================
echo Deployment wizard completed!
echo.
echo For detailed instructions, read DEPLOYMENT_GUIDE.md
echo.
pause