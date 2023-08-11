# Flask Testing
Project for trying out Python Flask. Implements a simple network model REST API.

## Setup
Install Python, create Python virtual environment, and activate it:

    $ python -m venv dev-env
    $ dev-env\Scripts\activate

Install dependencies

    $ pip install -r requirements.txt

Run the REST service

    $ FLASK_APP=nmm/app.py 
    $ python -m flask run

Run tests with code coverage (without end-to-end tests)

    $ python -m pytest tests  -m "not e2e" --cov=nmm

Run the end-to-end (e2e) tests:

    $ python nmm/init_db.py
    $ python -m pytest tests -m e2e