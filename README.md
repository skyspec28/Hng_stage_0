# Profile API with Cat Facts

A simple FastAPI application that provides a REST API endpoint returning profile information along with random cat facts.

## Features

- GET `/me` endpoint returning profile information
- Integration with Cat Facts API
- Dynamic timestamp in UTC
- Environment variable configuration
- CORS support
- Error handling

## Requirements

- Python 3.7+
- pip (Python package manager)

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your information:
     ```
     USER_EMAIL=your.email@example.com
     USER_NAME=Your Full Name
     USER_STACK=Python/FastAPI
     ```

## Running the Application

To run the application locally:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Test the API

You can test the endpoint using curl:

```bash
curl http://localhost:8000/me
```

Or visit `http://localhost:8000/me` in your web browser.

## API Documentation

Once the application is running, you can access the automatic API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Error Handling

The API implements proper error handling for:

- External API failures
- Network timeouts
- Server errors

## Dependencies

- FastAPI: Web framework
- uvicorn: ASGI server
- python-dotenv: Environment variable management
- httpx: HTTP client for API requests
