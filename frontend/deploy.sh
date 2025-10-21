#!/bin/bash

# Load environment variables from parent .env and current folder
set -a
source ../.env
[ -f .env ] && source .env
set +a

REGION="europe-west1"
SERVICE_NAME="nuxt-frontend"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

# Get the backend URL
BACKEND_URL=$(gcloud run services describe flask-backend --region=$REGION --format='value(status.url)' --project=$PROJECT_ID)

if [ -z "$BACKEND_URL" ]; then
  echo "Warning: Backend service not found. Using placeholder URL."
  BACKEND_URL="https://flask-backend-XXXXX.run.app"
fi

echo "Backend URL: $BACKEND_URL"

# Build the container image
echo "Building container image..."
gcloud builds submit --tag $IMAGE_NAME --project $PROJECT_ID

# Deploy to Cloud Run
echo "Deploying Nuxt frontend to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars "NUXT_PUBLIC_API_BASE=${BACKEND_URL}" \
  --project $PROJECT_ID \
  --port 3000

echo "Deployment complete!"
echo "Frontend URL: $(gcloud run services describe $SERVICE_NAME --region=$REGION --format='value(status.url)' --project=$PROJECT_ID)"
