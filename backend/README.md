# FastAPI Backend

This is the backend of the full-stack application built using FastAPI. The backend serves as the API layer, handling requests from the frontend and processing them accordingly.

## Features

- RESTful API built with FastAPI
- Dependency injection using Pydantic for data validation
- CORS middleware for handling cross-origin requests
- Integration with the Gemini API for AI command processing

## Directory Structure

- `app/`: Contains the main application code.
  - `main.py`: Entry point for the FastAPI application.
  - `api/`: Contains API-related code.
    - `v1/`: Version 1 of the API.
      - `routes.py`: Defines the API routes.
      - `deps.py`: Dependency injection functions.
  - `core/`: Core application configuration.
    - `config.py`: Configuration settings.
  - `models/`: Database models.
    - `user.py`: User model definition.
  - `schemas/`: Pydantic schemas for data validation.
    - `user.py`: User schema definition.
  - `crud/`: CRUD operations.
    - `crud_user.py`: User-related CRUD operations.
  - `db/`: Database-related code.
    - `base.py`: Base model for the database.
    - `session.py`: Database session management.
- `tests/`: Contains tests for the application.
  - `test_main.py`: Tests for the main application.
- `requirements.txt`: Lists the dependencies required for the backend.
- `.env`: Contains environment variables for the application.
- `Dockerfile`: Instructions for building the Docker image for the backend.

## Getting Started

1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables in the `.env` file.
5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## Testing

To run the tests, navigate to the `backend` directory and execute:
```
pytest tests/
```

## Docker

To build and run the Docker container for the backend, use the following commands:
```
docker build -t fastapi-backend .
docker run -d -p 8000:8000 fastapi-backend
```

## License

This project is licensed under the MIT License.