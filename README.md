# Pharmacy Management System (PMS) 💊

A comprehensive **E-commerce Pharmacy Management System** built using **Python and Django**, designed to streamline the online purchasing and management of pharmaceutical products.

## 🚀 Features

- **User Authentication** (Sign Up, Login, Logout)
- **Admin Dashboard** for managing products, orders, and users
- **Product Management** (Add, Edit, Delete Medicines)
- **Shopping Cart & Checkout** for seamless ordering
- **Order Management** (Track orders, view history)
- **Search & Filter** functionality for medicines
- **Secure Payment Integration** (Optional)
- **Responsive UI** for mobile and desktop users

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django Rest Framework (DRF)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL / SQLite
- **Deployment:** Heroku / AWS / DigitalOcean (Optional)

## 📌 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MeeranHusain/PMS.git
cd PMS
```

### 2️⃣ Set Up Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.


## 🛒 Usage
1. Sign up or log in as a customer or admin.
2. Browse available medicines and add them to the cart.
3. Proceed to checkout and place an order.
4. Admins can manage products, orders, and users via the admin dashboard.
