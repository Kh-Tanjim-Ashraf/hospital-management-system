# Hospital-Management-System

**OSTAD Assignment:** Hospital Appointment Management System API using Django REST Framework (DRF)

## Scenario

A small hospital wants a simple system where:

- Patients can register and book appointments.
- Doctors can view their appointments.
- Admin can manage doctors and appointments.
- The hospital can generate a simple dashboard summary.

There are three user roles:

- Admin
- Doctor
- Patient

## Project Setup Instructions

### Setup Python Virtual Environment

1. Create virtual environment inside the project directory.

   > python -m venv env

2. Activate the virtual enviroment.

   > Windows (CMD): .\env\Scripts\activate

   > Windows (bash): source env/Scripts/activate

   > MacOS/Linux: source env/bin/activate

3. Install the required packages from ["**requirements.txt**"](./requirements.txt) file.

   > pip install -r requirements.txt

### Configure .env File

1.  Create a "**.env**" file inside the project's base directory.

2.  Define the values according to the following keys inside the sample ["**.env-example**"](./.env-example) file.

## Required packages

      asgiref==3.12.1
      Django==6.0.7
      djangorestframework==3.17.1
      djangorestframework_simplejwt==5.5.1
      PyJWT==2.13.0
      python-dotenv==1.2.2
      sqlparse==0.5.5
      tzdata==2026.3

## How To Run The Project

### Run Development Server

**💡 Note: Python virtual environment is required to be activated in order to run the Django project in development server.**

\# Run the "**server.sh**" bash script in the terminal for automating the execution of database migration commands & eventually run the server in development mode at port 8080 in the host machine.

<small>The "**server.sh**" file is located inside the project directory.</small>

> bash server.sh

\# Create a superuser/admin to access the default admin panel for adminstration tasks.

> python manage.py createsuperuser

<small>💡 **Note:** Provide the **email, role, password** information in order to create a superuser through Django CLI.</small>

### Optional

\# To run this Django project inside the local machine, execute the following command.

> python manage.py runserver 8080

\# To execute only the database migrations through shell script.

> bash db_migration.sh

## High Level Design

[**Hospital-Management-System | ERD ➡️**](./doc-resources/diagrams/erd.md)

## API Endpoint List
