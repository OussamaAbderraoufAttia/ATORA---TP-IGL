# 📝 Django Project Setup Instructions

## 📁 Project Overview

This Django project includes:
- A Django backend
- Django Rest Framework for APIs
- Dependencies managed using `pip` and Pipenv
- Virtual environment (`venv`) setup

---

## 🔹 **Step 1: Clone the Repository**

Clone the project repository to your local machine:

git clone https://github.com/OussamaAbderraoufAttia/ATORA---TP-IGL/
Navigate into the project folder:

cd your-repository

---

## 🔹 **Step 2: Set Up the Virtual Environment**

Create and activate the virtual environment (recommended):

python -m venv venv

Activate the environment:

- **On Windows**:
  venv\Scripts\activate

- **On macOS/Linux**:
  source venv/bin/activate

---

## 🔹 **Step 3: Install Dependencies**

If you have a `Pipfile` (Pipenv):

pip install pipenv
pipenv install

OR if you have a `requirements.txt` file:

pip install -r requirements.txt

Verify installation:

pip freeze

---

## 🔹 **Step 4: Apply Migrations**

Run database migrations to set up your Django database:

python manage.py migrate

---

## 🔹 **Step 5: Create a Superuser (Optional)**

Create an admin user to access Django’s admin interface:

python manage.py createsuperuser

Follow the prompts to set your username and password.

---

## 🔹 **Step 6: Run the Django Server**

Start the Django development server:

python manage.py runserver

By default, the server will run at:

**Local URL**: http://127.0.0.1:8000/

---

## 🔹 **Step 7: Access Your Project**

- Open your browser and navigate to **http://127.0.0.1:8000/** to see your Django app.
- Use **http://127.0.0.1:8000/admin** to access the Django admin panel (if a superuser was created).

---

## 📜 **Common Issues & Fixes**

- **ModuleNotFoundError**:
  Ensure all dependencies are installed:

  pip install djangorestframework

- **Database Errors**:
  Apply migrations if you get database errors:

  python manage.py migrate

- **Environment Errors**:
  If Pipenv or virtual environment activation fails, deactivate any running environments first:

  deactivate

---

📚 For more details, refer to the Django documentation:  
https://docs.djangoproject.com/en/stable/
