# Hermes

Hermes is a self-hosted service for securely sharing API keys, passwords, secret messages, and small files. Inspired by Yopass, the project aims to provide time-limited and encrypted sharing of sensitive information.

## Features (Implemented)
- Secure sharing of text with time-based expiration.
- Encryption of all data before storage.
- Email notifications to recipients with a unique link and key (via SendGrid).
- Automatic cleanup of expired secrets using Celery Beat.

## Installation (Getting Started)
1. Clone this repository:
   ```powershell
   git clone https://github.com/<your-username>/hermes.git
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
6. Configure environment variables by creating a `.env` file:
   ```
   SENDGRID_API_KEY=your_sendgrid_api_key_here
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password_or_api_key
   ```
7. Start the Django development server:
   ```powershell
   python manage.py runserver
   ```
8. Start Celery Worker:
   ```powershell
   celery -A hermes worker --loglevel=info --pool=solo
   ```
9. Start Celery Beat:
   ```powershell
   celery -A hermes beat --loglevel=info
   ```

## Project Status
- [x] Initial Django project setup.
- [x] Secure text sharing with encryption.
- [x] Email notifications via SendGrid.
- [x] Automatic deletion of expired secrets using Celery.
- [ ] Improve frontend UI/UX.
- [ ] Evaluate Zero-Knowledge encryption model.

## Tech Stack
- Python (Django)
- PostgreSQL
- Celery + Redis (for background tasks)
- Django Celery Beat (for scheduled tasks)
- SendGrid API (for email notifications)

---

## Future Features
- User authentication via Google SSO or manual registration.
- Ability to save frequently used recipient addresses.
- Protection against denial-of-service attacks.
- Potential Google Drive integration for file sharing.

