# Twitor
Twitter browsing automation tool.

## Setup
```bash
$ cp .env.sample .env
```

Type in your twitter_id and password.
```bash
USER_ID="YOUR_TWITTER_ID"
PASSWORD="YOUR_TWITTER_PASSWORD"
```

## Run
```bash
$ pipenv shell
(twitor) $ pipenv install
(twitor) $ python3 sample.py
```

## Environment
| | |
| :--- | :--- |
| Python | 3.x |
| Package control | pipenv |
| Linter | flake8, mypy |
| Formatter | black |
