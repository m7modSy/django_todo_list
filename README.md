#Setting Up Virtual Environment & Installing Dependencies (Linux)

## Prerequisites
Ensure Python is installed. Check with:
python3 --version

## 1. Create Virtual Environment
python3 -m venv env

## 2. Activate Virtual Environment
source env/bin/activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Run Server
python3 manage.py runserver

The app is working now on http://127.0.0.1:8000/
