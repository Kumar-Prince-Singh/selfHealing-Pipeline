#!/bin/bash
# Usage: ./retry.sh "command to run" max_retries delay_seconds

COMMAND="$1"
MAX_RETRIES=${2:-3}
DELAY=${3:-5}

for i in $(seq 1 $MAX_RETRIES); do
    echo "Attempt $i of $MAX_RETRIES"
    if eval "$COMMAND"; then
        echo "Success!"
        exit 0
    else
        echo "Attempt $i failed. Waiting $DELAY seconds..."
        sleep $DELAY
        DELAY=$((DELAY * 2))  # Exponential backoff
    fi
done

echo "All $MAX_RETRIES attempts failed."
exit 1