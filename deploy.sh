#!/bin/bash

# Stop and remove old container if exists
docker rm -f library-app-container 2>/dev/null || true

# Pull latest image
docker pull devnotfound404/library-app:latest

# Run container
docker run -d \
  --env-file .env \
  -p 8000:8000 \
  --name library-app-container \
  devnotfound404/library-app:latest
