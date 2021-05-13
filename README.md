# Django-test-assignment

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>
A simple Django application where you can make queries to the database through a simple front-end interface.


## Getting Started <a name = "getting_started"></a>
To run the project locally.
1. Clone this repo
(Steps 2 - 4 are optional, but required if a user wishes to send the queried data to an email with PDF)
2. In djangobackend/settings.py, change the email to your email at 123
3. Scroll down to line 123 and change the email configuration to your own email (the current configuration has been set to gmail)
4. In invemtory/views.py line 26 has instructions for needed data
5. Cd into it.
6. pip install -r requirements.txt
7. run with command python manage.py runserver
8. go to you browser and insert http://127.0.0.1:8000/

## Usage <a name = "usage"></a>
To use the full functionality of this project you need to configure the email settings.py located in djangobackend folder.
In settings.py on line 123 is a small set of instructions how to configure the email.
Also in the inventory -> views.py from line 26 the user must configure the fields to send the email.

This project comes with a database, where a superuser has allready been created.

Username is: aetham
Password is: qwe123
