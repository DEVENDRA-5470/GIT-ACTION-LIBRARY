FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (required for mysqlclient + mysqladmin)
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    default-mysql-client \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy all project files including .env
COPY . .

# ✅ Explicitly copy the .env file again (just to be safe — optional)
COPY .env .env

# Run migrations and start the app
CMD ["sh", "-c", "python manage.py migrate && gunicorn Library_Management.wsgi:application --bind 0.0.0.0:8000"]
