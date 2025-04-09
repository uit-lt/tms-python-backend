#!/bin/bash

ENV_FILE=".env"
KEY_NAME="JWT_SECRET_KEY"

NEW_KEY=$(openssl rand -base64 64 | tr -d '=+/')

if grep -q "^$KEY_NAME=" "$ENV_FILE"; then
  sed -i.bak "s/^$KEY_NAME=.*/$KEY_NAME=$NEW_KEY/" "$ENV_FILE"
else
  echo "$KEY_NAME=$NEW_KEY" >> "$ENV_FILE"
fi

echo "✅ Updated .env file with new $NEW_KEY:"
echo

echo "📦 Rebuilding Docker containers..."
docker compose up -d --build
echo "✅ Updated .env file with new JWT_SECRET_KEY"
echo "📦 Rebuild Docker containers successfully"
