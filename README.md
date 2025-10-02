# Flask-Project

## Environment Variables

Create a `.env` file in the root directory:

```env
POSTGRES_DB=your_database
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
DATABASE_URL=postgresql://your_user:your_password@postgres:5432/your_database
OLLAMA_MODEL=your_model
```

## Getting Started

Start all services:

```bash
docker-compose up -d --build
```

Access the applications:

- Frontend: <http://localhost:3000>
- Backend API: <http://localhost:5000>
- Ollama: <http://localhost:11434>
- PostgreSQL: localhost:5432

## Development

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

## Services

- **backend**: Flask API server (port 5000)
- **frontend**: Nuxt.js application (port 3000)
- **ollama**: AI model server (port 11434)
- **db**: PostgreSQL database (port 5432)

## Stopping Services

```bash
docker-compose down
```
