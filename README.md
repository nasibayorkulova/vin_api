# VIN Decoder

This is a microservice that accepts a [VIN number](https://en.wikipedia.org/wiki/Vehicle_identification_number) from the exposed REST API endpoint, and return the following vehicle details by decoding the provided VIN.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/nasibayorkulova/vin_api.git
$ cd vin_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd vehicle_project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/`.

## Database

Starting pgAdmin4 server
Create a new database in PostgreSQL or change DB details to yours in settings.py

(venv) python manage.py makemigrations

(venv) manage.py migrate

(venv) manage.py createsuperuser
(example: admin/123)

And navigate to admin panel http://127.0.0.1:8000/admin/   with created login and password

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test gc_app
```

### API request-response

Send post request to http://127.0.0.1:8000/api/decode/   with vin in JSON format
{
    "vin": "1P3EW65F4VV300933"
}


To response you will get Vehice details for your VIN in JSON format:
{
    "vin": "1P3EW65F4VV300933",
    "year": "1997",
    "make": "Plymouth",
    "model": "Prowler",
    "type": "Gas V6",
    "color": "black",
    "dimensions": "4330x1690x1505",
    "weight": "1190"
}
