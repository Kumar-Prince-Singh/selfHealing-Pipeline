#!/bin/bash
# Continuous health monitoring

CONTAINER_NAME="my-app"

while true; do
    HEALTH=$(docker inspect --format='{{.State.Health.Status}}' $CONTAINER_NAME 2>/dev/null)
    
    if [ "$HEALTH" == "unhealthy" ]; then
        echo "⚠️ Container unhealthy! Restarting..."
        docker-compose restart $CONTAINER_NAME
        echo "✅ Container restarted at $(date)"
    elif [ "$HEALTH" == "" ]; then
        echo "Container not found. Starting..."
        docker-compose up -d
    fi
    
    sleep 30  # Check every 30 seconds
done