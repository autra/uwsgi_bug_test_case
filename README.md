# to use

## installation
```
virtualenv --python=python3 venv
cd app
pip install .
pip install uwsgi
```

## start

Working case: `./venv/bin/uwsgi  --yaml ./uwsgi.yml`

bug: `/venv/bin/uwsgi --yaml ./uwsgi_bug.yml`

make request against the `/test` route.
