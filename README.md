# QR Notes with JWT Authentication

This Django project allows you to create private notes, each accessible via a **JWT-secured QR code**. The QR code encodes a link to a private note, accessible only with a valid JWT token.

## Features

- Create private notes that are protected by JWT (JSON Web Token) authentication.
- Access private notes by scanning the QR code that links to the note, secured with JWT.
- Easy-to-use API for creating and accessing notes.

---

## Prerequisites

Ensure you have the following installed:

- Python (3.6 or higher)
- Django (3.0 or higher)
- Virtual environment (optional but recommended)
- SQLite (depending on your database)

Due this project requires UI component which is not included in repository cause the file size.
You can download the UI package directly from the following Google Drive link:

https://drive.google.com/file/d/1Yw6jpcNAVGMpua4cMzJwUPoGRMtlNKXu/view?usp=drive_link

### How to Add UI

1. Click the link above and download the UI zip file.
2. Extract the zip contents into the qr-notes/app/templates directory of this project.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/qr-notes.git
cd qr-notes
````

### 2. Create a Virtual Environment

**Using `venv`:**

```bash
python -m venv venv
```

**Activate the virtual environment:**

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

### 4. Set up the Database

If you are using SQLite (default), you don’t need to do anything. If you're using PostgreSQL, make sure you have the correct database configuration in your `.env` file.

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin access)

```bash
python manage.py createsuperuser
```

---

## Configuration

### 1. Environment Variables

You can configure your settings according to your environment:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
DATABASE_URL=sqlite:///db.sqlite3  # Or your database URL if using PostgreSQL
QR_BASE_URL=http://'0.0.0.0:8000  # Change this to your actual server URL
```

### 2. Install Dependencies

The project uses several dependencies, which can be installed by running:

```bash
pip install -r requirements.txt
```

Required dependencies:

* `django`: Web framework
* `PyJWT`: For handling JSON Web Tokens
* `qrcode`: For generating QR codes
* `Pillow`: For handling image generation

---

## Usage

### 1. Run the Development Server

To start the Django development server:

```bash
DJANGO_SETTINGS_MODULE=config.settings.dev python manage.py runserver 0.0.0.0:8000
```

You can now access your application by navigating to [http://localhost:8000](http://localhost:8000) or [http://'0.0.0.0:8000](http://'0.0.0.0:8000) (or whatever IP your machine is using on your local network).

### 2. Create a Private Note

To create a private note, you need to authenticate via JWT (using a token from a login endpoint or admin interface). Here’s a simple API example for creating a note:

#### Example API Request:

**POST** `/notes/create/`

```json
{
  "title": "My Private Note",
  "content": "This is a private note only accessible with a valid JWT token."
}
```

This will create a new note and return a unique token.

### 3. Generate QR Code for the Note

Once the note is created, a JWT token is generated and embedded in the URL that points to the specific note. You can use the JWT token to generate a QR code for the note.

Example of the URL with the JWT token:

```bash
http://'0.0.0.0:8000/notes/view/{token}/
```

Use the `qrcode` library to generate the QR code:

```python
import qrcode
from django.conf import settings

# URL to generate QR code for
url = f"{settings.QR_BASE_URL}/notes/view/{token}/"
qr = qrcode.make(url)

# Save or display the QR code
qr.save("note_qr.png")
```

You can then share the QR code with others. When someone scans it, they will be redirected to the private note — but only if they have a valid JWT token.

---

## Endpoints

* **POST /notes/create/**: Create a new note (requires JWT).
* **GET /notes/view/{token}/**: View a private note by token (requires JWT).

---

## Development

### Running the Development Server

```bash
DJANGO_SETTINGS_MODULE=config.settings.dev python manage.py runserver 0.0.0.0:8000
```

### Running Tests

To run the tests:

```bash
python manage.py test
```

---

## Project Structure

```bash
qr-notes/
│
├── config/                 # Django settings
│   ├── __init__.py
│   ├── base.py             # Common settings
│   ├── dev.py              # Development settings
│   └── prod.py             # Production settings
│
├── app/               # Application folder
│   ├── __init__.py
│   ├── models.py           # Models for notes
│   ├── views.py            # Views to handle note access and creation
│   ├── urls.py             # URL routing for the app
│   └── serializers.py      # Serializers for converting note data
│
├── manage.py               # Django management file
├── README.md               # Project README file
└── db.sqlite3              # SQLite database (if using SQLite)
```

---

## Screenshots

## Sample
![Alt text](/screenshots/landing_page.jpg)
![Alt text](/screenshots/create_note.jpg)
![Alt text](/screenshots/note_created.jpg)
![Alt text](/screenshots/view_note.jpg)
![Alt text](/screenshots/invalid_note.jpg)
![Alt text](/screenshots/how_to_use.jpg)
![Alt text](/screenshots/about.jpg)

## Deployment

For production deployment, it is recommended to:

1. Set `DEBUG=False`.
2. Use a production-ready web server like **Gunicorn** behind **NGINX**.
3. Configure PostgreSQL or another production-ready database.
4. Set up a secure HTTPS connection.