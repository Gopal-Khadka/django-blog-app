# Django Blog App

<!--toc:start-->
- [Django Blog App](#django-blog-app)
  - [Features](#features)
  - [TODO](#todo)
  - [Installation](#installation)
  - [Django Apps](#django-apps)
  - [Third Party Packages and Libraries](#third-party-packages-and-libraries)
  - [LICENSE](#license)
<!--toc:end-->

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

## TODO

- User Profile Customization and Personalization
- Better UI
- Badges,Achievements,Leaderboards and Analytics
- Social Media Integration(Share blogs on social media)
- Blog Feedback Polls
- Donation and Sponsorship

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

## Third Party Packages and Libraries

- `allauth`: For authentication(`eg:Google Authentication`)
- `easy-thumbnails`: For resizing images in django
- `django-filebrowser`: For file upload and browsing
- `grappelli`: For admin panel for file upload and browsing
- `tinymce`: For text editor in django
- `rest_framework`: For REST API to list,retrieve,create,update and delete blog articles
- `algoliasearch-django`: For search engine for blog articles
- `celery`: For sending emails daily or weekly using celery
- `faker`: For generating fake data for testing

## LICENSE

This project is licensed under the terms of the GNU Lesser General Public License, version 2.1. See [here](./LICENSE)
