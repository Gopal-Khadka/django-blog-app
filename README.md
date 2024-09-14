# Django Blog App

A blog web application built with Django for students trying to leave their home country to motivate them back to stay back in Nepal.

## Features

- Authentication and Authorization
- User(Authors) Profile Management
- Text editor for blog posts
- Blog post management(create, update, delete)
- Blog post search using Algolia Search
- Blog post comments and likes
- Discussion forum for students
- Email newsletters for the subscribed user using `Celery`
- Google Authentication
- Success stories for the student viewers

## Installation

```bash
python -m venv venv
```

Create a virtual environment for the project.

```bash
source venv/Scripts/activate
```

Activate the virtual environment.

```bash
pip install -r requirements.txt
```

All the necessary packages are installed in your virtual environment.

```bash
cd backend
```

All the python django files are in the `backend` folder.

```bash
python manage.py runserver
```

Open http://localhost:8000 in your browser. Enjoy.

## Django Apps

- `blogs`: A blog web application built with Django
- `api`: A REST API built with Django rest framework
- `forum`: A forum for students
- `stories`: A success stories for the student
