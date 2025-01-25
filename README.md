# Hermes

Hermes is a self-hosted service for securely sharing API keys, passwords, secret messages, and small files. Inspired by Yopass, the project aims to provide time-limited and encrypted sharing of sensitive information.

## Features (In Progress)
- Secure sharing of text and files with time-based expiration.
- Encryption of all data before storage.
- Email notifications to recipients with a unique link and key.

## Installation (Getting Started)
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/hermes.git
   cd hermes
   ```
2. Create a virtual Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Status
- [x] Initial Django project setup.
- [ ] Add functionality for secure text sharing.
- [ ] Integrate Google Drive for file sharing.
- [ ] Create a user-friendly frontend.

## Tech Stack
- Python (Django)
- PostgreSQL
- Google Drive API (for file handling)

---

## Future Features
- User authentication via Google SSO or manual registration.
- Ability to save frequently used recipient addresses.
- Protection against denial-of-service attacks.

