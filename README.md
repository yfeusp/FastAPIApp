# FastAPI App

A lightweight FastAPI application with a health check endpoint, designed to be deployed as a containerized service with multiple replicas.

## Project Structure

```
FastAPIApp/
├── app/
│   ├── __init__.py
│   └── main.py            # FastAPI application & endpoints
├── Dockerfile              # Production container image
├── .dockerignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.14+
- Docker (for containerized deployment)

## Local Environment Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd FastAPIApp
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

5. **Run the tests**

   ```bash
   pytest tests/ -v
   ```

## API Endpoints

| Method | Path      | Description                                              |
|--------|-----------|----------------------------------------------------------|
| GET    | `/health` | Returns service status, hostname, and UTC timestamp      |
| GET    | `/docs`   | Interactive API documentation (Swagger UI, auto-generated) |

### Example Response

```bash
curl http://localhost:8000/health
```

```json
{
  "status": "healthy",
  "hostname": "my-pod-abc123",
  "timestamp": "2026-10-03T20:00:00.000000+00:00"
}
```

> The `hostname` field is useful for verifying which replica is serving the request behind a load balancer.

## Docker

### Build the image

```bash
docker build -t fastapi-app .
```

### Run a container

```bash
docker run -d -p 8000:8000 fastapi-app
```

## Deployment Notes

- The container runs a **single Uvicorn worker** by design. Horizontal scaling should be handled by the orchestrator (e.g., Kubernetes replicas).
- The `/health` endpoint can be used as a **readiness/liveness probe** in Kubernetes.
- The application is **stateless**, so it scales horizontally without any shared state concerns.
