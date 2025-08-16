FROM python:3.12-slim


WORKDIR /app


RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV SECRET_KEY="django-insecure-h3=(x#$pj@&8g^p0ke0*z)c4-53ec^15qq!i#njb-@5m42@hz@"
ENV CELERY_BROKER_URL="redis://localhost:6379"
ENV CELERY_BACKEND="redis://localhost:6379"


RUN mkdir -p /app/static /app/staticfiles /app/media


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "config.wsgi:application"]