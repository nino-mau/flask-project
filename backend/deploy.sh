#!/bin/bash

# Load environment variables from parent .env and current folder
set -a
source ../.env
[ -f .env ] && source .env
set +a

REGION="europe-west1"
SERVICE_NAME="flask-backend"

# Create secrets in Secret Manager
echo "Creating secrets in Secret Manager..."
echo -n "$CLOUD_DB_PASSWORD" | gcloud secrets create CLOUD_DB_PASSWORD --data-file=- --project=$PROJECT_ID 2>&1 | grep -v "already exists" || true
echo -n "$OPENROUTER_API_KEY" | gcloud secrets create OPENROUTER_API_KEY --data-file=- --project=$PROJECT_ID 2>&1 | grep -v "already exists" || true
echo -n "$CLOUDINARY_API_SECRET" | gcloud secrets create CLOUDINARY_API_SECRET --data-file=- --project=$PROJECT_ID 2>&1 | grep -v "already exists" || true

# Grant service account access to secrets
echo "Granting secret access to service account..."
gcloud secrets add-iam-policy-binding CLOUD_DB_PASSWORD \
  --member="serviceAccount:flask-backend@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

gcloud secrets add-iam-policy-binding OPENROUTER_API_KEY \
  --member="serviceAccount:flask-backend@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

gcloud secrets add-iam-policy-binding CLOUDINARY_API_SECRET \
  --member="serviceAccount:flask-backend@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

# Deploy to Cloud Run
echo "Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --service-account flask-backend@${PROJECT_ID}.iam.gserviceaccount.com \
  --add-cloudsql-instances $INSTANCE_CONNECTION_NAME \
  --set-env-vars "INSTANCE_CONNECTION_NAME=$INSTANCE_CONNECTION_NAME,POSTGRES_USER=$POSTGRES_USER,POSTGRES_DB=$POSTGRES_DB,OLLAMA_MODEL=$OLLAMA_MODEL,OPENROUTER_MODEL=$OPENROUTER_MODEL,CLOUDINARY_NAME=$CLOUDINARY_NAME,CLOUDINARY_API_KEY=$CLOUDINARY_API_KEY" \
  --set-secrets "CLOUD_DB_PASSWORD=CLOUD_DB_PASSWORD:latest,OPENROUTER_API_KEY=OPENROUTER_API_KEY:latest,CLOUDINARY_API_SECRET=CLOUDINARY_API_SECRET:latest" \
  --project $PROJECT_ID

echo "Deployment complete!"
