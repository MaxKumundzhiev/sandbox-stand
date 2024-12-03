# Users Database Migrations
*initialize almbic*
```bash
$ alembic init -t async users-db-migrations
```

*generate migration*
```bash
$ alembic revision --autogenerate -m "create users table"
```

*apply migration*
```bash
$ alembic upgrade head
```