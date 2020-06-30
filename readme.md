# Management application

A web application build on Django 2.2.13, CSS and Bootstrap for templates and PostgreSQL

**Requirements**

1. Python 3.x.x
2. Django 2.2.13
3. Bootstrap 3 ( Files are already downloaded in project directory)
4. PostgreSQL 12.3 & pgAdmin4

# Getting Started

- Clone this repository by this command.

  `git clone https://github.com/Badhan-abhishek/management-application-django`

- Open terminal or CMD in directory where **manage.py** exists.
- Change SECRET_KEY & database password in **Settings.py**
- Create a superuser with command `python3 manage.py createsuperuse`
- Run migrations by following commands.

1.  `python3 manage.py makemigrations`
2.  `python3 manage.py sqlmigrate [application name] [migration number]`
3.  `python3 manage.py migrate`

- At last run server by following command `python3 manage.py runserver`

> **NOTE :-** \
>
> - Windows user need to use `python manage.py [command]` \
> - Application name is manageApp

# Usage

This application can be used for various body management systems with few tweaks.

- It can be used for student management
- It can be used for employee management
