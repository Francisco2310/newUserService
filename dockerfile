FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir poetry \
&& poetry config virtualenvs.create false \
&& poetry install --no-root --no-interaction --no-ansi
WORKDIR /app/src/newuserservice
CMD ["sh", "-c", "python -m flask db upgrade && gunicorn -w 4 -b 0.0.0.0:8000 app:app"]
EXPOSE 8000