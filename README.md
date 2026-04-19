# Flask Blog

A Flask CRUD blog application with PostgreSQL, Docker, and CI/CD.

## Setup

```bash
cd flask-blog
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
export FLASK_ENV=development
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/flask_blog_dev
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python app.py
```

## Run Tests

```bash
pytest tests/ -v
```

## Run with Docker

```bash
docker-compose up -d --build
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts` | List all posts |
| GET | `/api/posts/<id>` | Get single post |
| POST | `/api/posts` | Create post |
