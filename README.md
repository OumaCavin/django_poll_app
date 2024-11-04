
# Django Poll Application

This is a simple poll application built with Django. Users can create, view, and vote on polls.

## Project Structure

```plaintext
django_tutorial/
    ├── poll_app/
    │   ├── db.sqlite3
    │   ├── manage.py
    │   ├── poll_site/
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── asgi.py
    │   │   └── wsgi.py
    │   └── polls/
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── migrations/
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       ├── views.py
    │       └── urls.py
    ├── poll_env/
    │   ├── Include/
    │   ├── Lib/
    │   └── Scripts/
    └── .gitignore
```

## Features

- Users can view a list of polls
- Users can vote on polls
- Basic Django admin panel for managing polls

## Prerequisites

- Python 3.x
- Django 5.1.2
- Git (for version control)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/OumaCavin/django_poll_app.git
cd django_tutorial
```

### 2. Set up a virtual environment

```bash
python -m venv poll_env
```

### 3. Activate the virtual environment

- **Windows**:
  ```bash
  .\poll_env\Scripts\activate
  ```
- **MacOS/Linux**:
  ```bash
  source poll_env/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install django
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application should now be running at `http://127.0.0.1:8000/`.

## Usage

1. Visit the admin panel at `http://127.0.0.1:8000/admin/` to create polls. (You'll need to create a superuser first using `python manage.py createsuperuser`.)
2. Go to `http://127.0.0.1:8000/polls/` to view and vote on polls.

## Project Setup

- `poll_app/`: Contains the Django application code.
- `poll_env/`: Virtual environment directory.
- `db.sqlite3`: SQLite database file.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.


