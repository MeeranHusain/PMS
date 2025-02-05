# Pharmacy Management System (PMS)

## Overview
The **Pharmacy Management System (PMS)** is an e-commerce web application designed to streamline pharmacy operations by providing a platform to manage medicines, orders, users, and transactions efficiently. Built using **Python, Django, HTML, CSS, JavaScript, and MySQL**, this system ensures seamless pharmacy management.

## Features
- **User Authentication & Authorization** (Admin, Pharmacist, Customer)
- **Product Management** (Add, Edit, Delete Medicines)
- **Order Management** (Place, Track, Update Orders)
- **Inventory Management** (Stock Levels, Expiry Alerts)
- **Secure Transactions** (Online Payment Integration)
- **Admin Dashboard** (Analytics & Reports)
- **Responsive UI** (Tailwind CSS, Bootstrap for styling)

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap, Tailwind CSS
- **Backend:** Python, Django
- **Database:** MySQL
- **Deployment:** (Optional: Docker, AWS, Heroku, etc.)

## Installation
### Prerequisites
Ensure you have **Python 3.x**, **Django**, and **MySQL** installed.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/MeeranHusain/PMS.git
   cd PMS
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure the database:
   - Update `settings.py` with your MySQL credentials.
   - Run migrations:
     ```sh
     python manage.py makemigrations
     python manage.py migrate
     ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
   Access the application at **http://127.0.0.1:8000/**

## Usage
1. **Admin Panel:** `http://127.0.0.1:8000/admin/` (Login with superuser credentials)
2. **Manage Products & Users:** Add, edit, or delete medicines and manage customers.
3. **Place Orders:** Customers can browse, add to cart, and checkout securely.
4. **Track Orders:** Admins and customers can view order statuses in real-time.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests to improve the system.

## License
This project is licensed under the **MIT License**.

## Contact
For queries, reach out to [Meeran Husain](https://github.com/MeeranHusain)

