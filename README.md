# sarva_backend_assignment
Backend assignment implementation for sarva suvidhan company using Django and PostgreSQL

This project implements two backend APIs using Django and PostgreSQL, integrated with a Flutter frontend.

Tech Stack
Backend Framework: Django (Python)

Database: PostgreSQL

Frontend: Flutter https://github.com/s2pl/KPA-ERP-FE/

API Client: Postman

Implemented APIs
1. Submit Wheel Specification (POST)
URL: /api/wheel-specification/submit/

Method: POST

Functionality: Receives wheel specification data from Flutter frontend and stores it in PostgreSQL.

Status: Implemented & working

2. Get Wheel Specification (GET)
URL: /api/wheel-specification/

Method: GET

Functionality: Returns a list of all wheel specifications stored in the database.

Status: Implemented & working

3. Submit Bogie Checksheet (POST)
URL: /api/bogie-checksheet/submit/

Method: POST

Functionality: Receives and stores bogie checksheet form data from the Flutter app.

Status: Implemented & working

