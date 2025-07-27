#!/bin/bash

start_time=$(date +%s)
set -e

echo "📁 Ensuring 'static/' directory exists..."
mkdir -p static

echo "🔄 Stopping existing containers..."
docker-compose down

echo "🔧 Building images..."
docker-compose build

echo "🚀 Starting containers..."
docker-compose up -d

echo "⏳ Waiting for MySQL to be ready..."
until docker-compose exec db mysqladmin ping -h"127.0.0.1" -uroot -proot --silent; do
    printf "."
    sleep 5
done
echo -e "\n✅ MySQL is ready!"

echo "🔍 Checking if web container is running..."
if docker-compose ps web | grep -q "Up"; then
    echo "🛠️ Applying migrations..."
    docker-compose exec web python manage.py migrate --noinput

    echo "🎯 Collecting static files..."
    docker-compose exec web python manage.py collectstatic --noinput
else
    echo "❌ Web container is not running. Check logs with: docker-compose logs web"
    exit 1
fi

end_time=$(date +%s)
elapsed=$((end_time - start_time))

PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)
echo "🌐 Your app should be live at: http://$PUBLIC_IP"
echo "⏱️ Total deployment time: ${elapsed} seconds"

if command -v xdg-open >/dev/null; then
    xdg-open "http://$PUBLIC_IP"
elif command -v open >/dev/null; then
    open "http://$PUBLIC_IP"
else
    echo "🔗 Open in your browser: http://$PUBLIC_IP"
fi

echo "✅ Deployment complete!"
