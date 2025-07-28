#!/bin/bash

start_time=$(date +%s)
set -e

echo "📁 Ensuring 'static/' directory exists..."
mkdir -p static

echo "🔄 Stopping existing containers..."
sudo docker-compose down

echo "🔧 Building images..."
sudo docker-compose build

echo "🚀 Starting containers..."
sudo docker-compose up -d

echo "⏳ Waiting for MySQL to be ready..."
until sudo docker-compose exec -T db mysqladmin ping -h"127.0.0.1" -uroot -proot --silent; do
    printf "."
    sleep 5
done
echo -e "\n✅ MySQL is ready!"

echo "🔍 Checking if web container is running..."
if sudo docker-compose ps web | grep -q "Up"; then
    echo "🛠️ Applying migrations..."
    sudo docker-compose exec -T web python manage.py migrate --noinput

    echo "🎯 Collecting static files..."
    sudo docker-compose exec -T web python manage.py collectstatic --noinput
else
    echo "❌ Web container is not running. Check logs with: sudo docker-compose logs web"
    exit 1
fi

end_time=$(date +%s)
elapsed=$((end_time - start_time))

PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)
APP_URL="http://$PUBLIC_IP"
echo "🌐 Your app should be live at: $APP_URL"
echo "⏱️ Total deployment time: ${elapsed} seconds"

# Auto-open in browser
echo "🌐 Opening app in browser..."
sleep 3

if grep -qEi "(Microsoft|WSL)" /proc/version &> /dev/null; then
    echo "🪟 Detected WSL — using powershell.exe..."
    powershell.exe /C "start $APP_URL"
elif command -v xdg-open >/dev/null; then
    echo "🐧 Detected Linux — using xdg-open..."
    xdg-open "$APP_URL" 2>/dev/null || echo "❌ xdg-open failed. Open manually: $APP_URL"
elif command -v open >/dev/null; then
    echo "🍏 Detected macOS — using open..."
    open "$APP_URL" 2>/dev/null || echo "❌ open failed. Open manually: $APP_URL"
else
    echo "❌ No known browser launcher found. Please open manually: $APP_URL"
fi

echo "✅ Deployment Done"
