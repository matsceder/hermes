# Hermes

Hermes is a self-hosted service for securely sharing API keys, passwords, secret messages, and small files. Inspired by Yopass, the project aims to provide time-limited and encrypted sharing of sensitive information.

## Features (In Progress)
- Secure sharing of text and files with time-based expiration.
- Encryption of all data before storage.
- Email notifications to recipients with a unique link and key.
- Automatic cleanup of expired secrets using Celery Beat.

## Installation (Getting Started)
1. Clone this repository:
   ```powershell
   git clone https://github.com/matsceder/hermes.git
   cd hermes
   ```
2. Create a virtual Python environment:
   ```powershell
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```powershell
   python manage.py migrate
   ```
5. Create a superuser account (for Django Admin access):
   ```powershell
   python manage.py createsuperuser
   ```
6. Start the Django development server:
   ```powershell
   python manage.py runserver
   ```
7. Start Celery Worker:
   ```powershell
   celery -A hermes worker --loglevel=info --pool=solo
   ```
8. Start Celery Beat:
   ```powershell
   celery -A hermes beat --loglevel=info
   ```

## Project Status
- [x] Initial Django project setup.
- [x] Add functionality for secure text sharing.
- [x] Automatic deletion of expired secrets using Celery.
- [ ] Integrate Google Drive for file sharing.
- [ ] Create a user-friendly frontend.

## Tech Stack
- Python (Django)
- PostgreSQL
- Celery + Redis (for background tasks)
- Django Celery Beat (for scheduled tasks)
- Google Drive API (for file handling, future feature)

---

## Future Features
- User authentication via Google SSO or manual registration.
- Ability to save frequently used recipient addresses.
- Protection against denial-of-service attacks.

