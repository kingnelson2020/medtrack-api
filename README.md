# MedTrack API

A patient health tracking REST API built with Django and PostgreSQL.

## Live API
https://medtrack-api-production.up.railway.app

## Endpoints
- POST /api/login/ — get authentication token
- GET /api/patients/ — list all patients (requires token)
- POST /api/patients/ — create a patient (requires token)
- GET /api/patients/{id}/ — get single patient (requires token)
- PUT /api/patients/{id}/ — update a patient (requires token)
- DELETE /api/patients/{id}/ — delete a patient (requires token)

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- Deployed on Railway