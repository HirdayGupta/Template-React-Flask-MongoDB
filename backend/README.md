# Setup instructions

1. Create virtual environment

```
$ python3 -m venv .env
```

2. Activate virtual environment

```
$ source .env/bin/activate
```

3. Install requirements

```
$ pip install -r requirements.txt
```

# Run locally

Make sure your the virtual environment set up above is active, then run the following command

```
gunicorn --workers=5 --threads=2 wsgi
```

The API is now available at http://localhost:8000