# LAB - Class 28

## Project: Django CRUD

### Author: [Caleb Hemphill](https://github.com/kaylubh)

A small project to demonstrate how to set up a web app using Django with a model to dynamically render web pages styled with Tailwind CSS. Additionally, implements basic CRUD operations.

### Setup

#### Requirements

1. Install [Python](https://www.python.org/) if not already

1. Create and activate a virtual environment

    `python3 -m venv .venv`

    `source .venv/bin/activate` (Linux/Mac)

    `source .venv/Scripts/activate` (Windows)

1. Install packages

    `pip install -r requirements.txt`

1. ***OPTIONAL*** Install/Setup Tailwind CSS

    *Not required to run the web app, required to make edits to the CSS*

    1. `npm install`
    1. In a standalone terminal run:

        `npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch`

#### Run

1. Run `python manage.py runserver` in order to run the Django development server and view the web app from root of project directory.

1. Navigate to the link provided on run:

    Should be similar to: `Starting development server at http://127.0.0.1:8000/`

#### Tests

From root of project directory run `python manage.py test`
