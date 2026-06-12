# Movies
## A simple movie database

To build the app and run it create a virtual enviornment:

> $ python -m venv .venv

Activate it on Windows:

> $ \Scripts\activate

Activate it on Linux/Mac:

> $ /bin/activate

Install build package and build the package:

> $ pip install build

> $ python -m build --wheel

This will create a file in the dist folder:

> dist/moviedb-1.0.0-py2.py3-none-any.whl

Install it with pip:

> $ pip install moviedb-1.0.0-py2.py3-none-any.whl

Create two files in the moviedb directory on Windows:

> $ echo sqlite:///database.db > database_uri

> $ echo 12345 > secret_key

Create two files in the moviedb directory on Linux/Mac:

> cat sqlite:///database.db > database_uri

> cat 12345 > secret_key 

Run it with the following command:

> $ flask --app moviedb run --debug

Then you see this output:

 > * Running on http://127.0.0.1:5000

Point your browser to http://127.0.0.1:5000

Now you can register users and login, after loggin in you can create movie entries.

