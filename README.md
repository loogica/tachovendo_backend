# Installing

## Dependencies

```sh
pip install -r requirements/local.txt
```

## Database

Configure `DATABASE` on `tachovendo_proj/settings/base.py`

```sh
make server_dbinitial
make migrate
make runserver
```

## Tests

```sh
make test
```
