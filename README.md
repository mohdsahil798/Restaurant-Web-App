<<<<<<< HEAD
# bt125
=======
# 🍽️ Restaurant Management Web App

## 📌 About the Project
This is a **Restaurant Management Web Application** built using **Django and Django REST Framework**. It helps restaurant owners manage menus, orders, customers, and staff efficiently.

## 🚀 Features
- 🍔 **User Authentication** (Signup, Login, Logout)
- 📜 **Menu Management** (Add, Update, Delete Dishes)
- 🛒 **Order Management** (Place, Track, Cancel Orders)
- 🧾 **Billing & Payments** (Generate Bills)
- 👥 **Role-Based Access** (Admins, Staff, Customers)
- 📡 **REST API** for seamless integration with frontend and third-party services

## 🛠️ Technologies Used
- **Backend:** Django, Django REST Framework (DRF)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite / PostgreSQL
- **Authentication:** Django Auth System / JWT Tokens

## 🔧 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohdsahil798/Restaurant-Web-App.git
   
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/

