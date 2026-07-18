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

3. Install the dependencies from "**requirements.txt**" file.

   > pip install -r requirements.txt

### Configure .env File

1.  Create a "**.env**" file inside the project's base directory.

2.  Define the values accordingly to the following keys inside the file.

        # Django
        SECRET_KEY=
        DEBUG=True

        # Database
        DB_ENGINE=
        DATABASE=
        DB_USER=
        DB_PASSWORD=
        DB_HOST=
        DB_PORT=

## How To Run The Project

### Run Development Server

**💡 Note: Python virtual environment is required to be activated in order to run the Django project in development server.**

\# Run the "**server.sh**" bash script in the terminal for automating the execution of database migration commands & eventually run the server in development mode at port 8080 in the host machine.

<small>The "**server.sh**" file is located inside the project directory.</small>

    > bash server

### Optional

\# To run this Django project inside the local machine, execute the following command.

    > python manage.py runserver 8080

## API Endpoint List
