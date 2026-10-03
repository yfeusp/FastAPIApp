import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI App",
    version="1.0.0",
)


@app.get("/health")
def health():
    """Health check endpoint.

    Returns the hostname so you can verify which replica
    is serving the request behind a load balancer.
    """
    return {
        "status": "healthy",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info")
def info():
    """Static info endpoint to test deployment."""
    return {
        "message": "Welcome to FastAPI on Kubernetes!",
        "author": "Yusdanis",
        "app_name": "FastAPIApp",
        "version": "1.0.0"
    }
