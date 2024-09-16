Employee Management Application
This project is a Django-based Employee Management System that allows users to add, update, and delete employee profiles. Certain fields, such as salary and designation, are locked after initial submission to ensure data integrity.

Features
Add Employee Information: Use a form to create employee profiles.
Unique Employee Profiles: Each employee has a unique profile.
View All Employees: Employees are listed on the homepage with their name, designation, and a short description.
Update Employee Information: Update employee details except for salary and designation after the profile is created.
Delete Employee Profile: Delete employees from the system.
Authentication: User authentication is implemented, with the ability to log in and log out.
Superuser: A superuser can manage all the employee profiles and perform administrative tasks.


Installation
Clone the Repository:

bash
Copy code
git clone <[repository-url](https://github.com/ByazidBostami/Employee_management_System)>
cd employee_management
Create a Virtual Environment:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies:


pip install -r requirements.txt
Run Migrations:


python manage.py migrate
Create a Superuser: To create a superuser, run:


python manage.py createsuperuser --username admin --email byazid.me@gmail.com
Set the password as 123 to comply with the assignment requirements.

Run the Server:


python manage.py runserver
Access the Application: Open your browser and go to: http://127.0.0.1:8000/


Usage
Navigation
Home: Lists all employee profiles.
Add Employee: Navigate to the "Add Employee" page to create a new employee.
Update/Delete Employee: Update existing employee information or delete employee profiles.
Login/Logout: Use the login/logout feature to access the application with superuser credentials.
Form Fields
Employee Form:
Name (Text)
Address (Text)
Phone (Text) - validation ensures only digits are accepted.
Salary (Non-editable after creation)
Designation (Non-editable after creation)
Short Description (Text area)
Restrictions
Salary and Designation: These fields are locked after the employee profile is created to prevent unauthorized changes.
Validation
Phone number validation ensures the field contains only digits.
Superuser Credentials
Username: admin
Password: 123
These credentials are required to log in and manage employee profiles.


