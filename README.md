# Project Management System (PMS)

## Overview
The **Project Management System (PMS)** is a web-based application built using **Python** and **Django** that helps users manage and track projects efficiently. It provides functionality for task assignments, progress tracking, and collaboration among team members.

## Features
- User authentication and role-based access control
- Create, update, and delete projects
- Assign tasks to team members
- Track project progress
- Notifications and alerts for task updates
- Dashboard with project insights

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (latest version)
- MySQL

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/MeeranHusain/PMS.git
   ```
2. Navigate to the project directory:
   ```sh
   cd PMS
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure the database in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
6. Run migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```sh
   python manage.py runserver
   ```
9. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Admins can create and manage projects.
- Users can be assigned tasks and update progress.
- Dashboard displays key project statistics.
- Notifications keep users updated on task changes.

## Contribution
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the **MIT License**.

## Contact
For any queries or support, reach out to **[Meeran Husain](https://github.com/MeeranHusain)**.

---

Enjoy building with PMS! 🚀

