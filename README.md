# CodeReview
To improve quality of code review this service was initiated as file storage with lint function.



`.env` file must be added and must contain:
```
DJANGO_HOST="0.0.0.0" # default 0.0.0.0 for local access
DJANGO_PORT="8000" # default 8000

SECRET_KEY_DJANGO="some-long-string"

EMAIL_HOST_USER="example@example.com"
EMAIL_HOST_PASSWORD="your-api-email-password"

POSTGRES_USER="example"
POSTGRES_PASSWORD="example"
POSTGRES_PORT="5432" # default 5432
POSTGRES_DB="example_db"

REDIS_USER="example"
REDIS_PORT="6379" # default 6379
REDIS_PASSWORD="some-number-of-symbols"
```