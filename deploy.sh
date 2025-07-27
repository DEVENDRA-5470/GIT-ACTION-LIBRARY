#!/bin/bash

set -e  # Exit if any command fails
START_TIME=$(date +%s)

echo "🔄 Stopping running containers..."
docker-compose down

echo "🔧 Building Docker images..."
docker-compose build

echo "🆙 Starting containers (detached)..."
docker-compose up -d

echo "🛠️ Running Django migrations..."
docker-compose exec web python manage.py migrate --noinput

echo "🎯 Collecting static files..."
docker-compose exec web python manage.py collectstatic --noinput

# Get public IP of the server
PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)
echo "🌐 Your app should be live at: http://$PUBLIC_IP"

# Optional: Auto open in browser based on OS
if command -v xdg-open >/dev/null; then
    echo "🌍 Opening in browser..."
    xdg-open "http://$PUBLIC_IP"
elif command -v open >/dev/null; then
    echo "🌍 Opening in browser..."
    open "http://$PUBLIC_IP"
else
    echo "🖐️ Please manually open: http://$PUBLIC_IP"
fi

END_TIME=$(date +%s)
ELAPSED_TIME=$((END_TIME - START_TIME))
echo "⏱️ Total deployment time: ${ELAPSED_TIME} seconds"

echo "✅ Deployment complete!"
