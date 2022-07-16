# Django REST

Used Django Rest Framework for creating some REST APIs

## Features
- Create Profile
- View Profile
- Update Profile
- Delete Profile (Soft Deletion)
- Upload Resume
- Change Resume (Old one not deleted)
- User Authentication

## Tech

- [Django Rest Framework] - For creating REST APIs!

## Procedure

- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     #   aviate_backend
    ```
- Create a new virtual environment and activate it.
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
- Copy .env file
   ```
   cp .env.example .env
   ```
- Make database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```
