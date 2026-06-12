# Movies.
## A simple movie database.

To build the app run create a virtual enviornment:.
$ python -m venv .venv

Activate it on Windows:.
$ \Scripts\activate

Activate it on Linux/Mac:.
$ /bin/activate

Install build package and build the package:.
$ pip install build
$ python -m build --wheel

This will create a file in the dist folder:.
dist/moviedb-1.0.0-py2.py3-none-any.whl

Install it with pip:.
pip install moviedb-1.0.0-py2.py3-none-any.whl
