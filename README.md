# Movies
## A simple movie database written in Flask and Pico CSS

First install git and python.

Clone this repository:

> $ cd <home_dir>

> $ git clone https://github.com/maxpa1n87/movies.git

> $ cd movies

To build the app and run it create a virtual enviornment:

> $ python -m venv .venv

Activate it on Windows:

> $ .venv\Scripts\activate

Activate it on Linux/Mac:

> $ source .venv/bin/activate

Generate a secret key:
> $ python

> $ >>> import secrets

> $ >>> print(secrets.token_hex())

> $ 159e168b2f39239958da822999d645d2121ef4ce072fb68698f1dfd2dccc6696

Adjust settings either in default_settings.py or make a copy and supply:

Linux/Mac:
> $ export MOVIEDB_SETTINGS=/path/to/settings.py

Windows:
> $ set MOVIEDB_SETTINGS=C:\path\to\settings.py

Install build package and build the package:

> $ pip install build

> $ python -m build --wheel

This will create a file in the dist folder:

> dist/moviedb-1.0.0-py2.py3-none-any.whl

Install it with pip:

> $ pip install moviedb-1.0.0-py2.py3-none-any.whl

Install waitress:

> pip install waitress

Run it with the following command:

> $ waitres-serve --host 127.0.0.1 --call moviedb:create_app

Then you see this output:

> INFO:waitress:Serving on http://127.0.0.1:8080

Point your browser to http://127.0.0.1:8080

Optional:

Install nginx and configure it as a reverse proxy using this tutorial:

https://flask.palletsprojects.com/en/stable/deploying/nginx/

Now you can register users and login, after loggin in you can create movie entries.
