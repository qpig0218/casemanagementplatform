# Chronic Disease Management Platform

This repository provides a minimal skeleton for a chronic disease management platform. It demonstrates a microservice-based backend using FastAPI and a placeholder for a frontend built with React.

## Structure

- `backend/` – contains a simple FastAPI service for patient management.
- `frontend/` – placeholder directory for a React application.
- `docker-compose.yml` – demonstrates how to run services using Docker.

## Running the backend

```
cd backend
pip install -r requirements.txt
uvicorn patient_service.main:app --reload
```

The server will start on `http://localhost:8000` with a simple patients API.

## Future work

This skeleton can be expanded with additional services, authentication, notifications, data integration, and a full frontend UI as described in the design proposal.
