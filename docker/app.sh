#!/bin/bash
alembic upgrade head

gunicorn  books_library.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000