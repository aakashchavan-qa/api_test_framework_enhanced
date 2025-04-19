@echo off
echo 🔧 Creating virtual environment...
python -m venv venv

echo ✅ Activating virtual environment...
call venv\Scripts\activate

echo 📦 Installing dependencies...
pip install -r requirements.txt

echo 🎭 Installing Playwright browsers...
python -m playwright install

echo 💡 Installing Allure CLI via NPM...
npm install -g allure-commandline

echo 🚀 All set! Run your tests with:
echo     pytest
