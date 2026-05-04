#!/bin/bash
# Rolls back to previous Docker image

PREVIOUS_IMAGE=$1
CURRENT_IMAGE=$2

echo "⚠️ Rolling back from $CURRENT_IMAGE to $PREVIOUS_IMAGE"

# Stop current container
docker-compose down

# Update docker-compose with previous image
sed -i "s|$CURRENT_IMAGE|$PREVIOUS_IMAGE|g" docker-compose.yml

# Start previous version
docker-compose up -d

echo "✅ Rollback complete. Previous version running."