# HNG 13 Backend Track Stage 0

A publicly accessible RESTful API that returns my profile information along with a dynamic cat fact fetched from an external API. Implementation was achieved using Python's FastAPI framework.

## Local Setup

Clone the repository:

```bash
git clone https://github.com/skyspec28/Hng_stage_0.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
# On Windows
source venv/Scripts/activate

# On Linux and Mac
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies available in requirements.txt:

- fastapi
- uvicorn
- httpx
- python-dotenv

## Running the Application

Run the application locally:

```bash
uvicorn app.main:app --reload
```

## API Documentation

### Typical JSON Response Format (200 OK):

```json
{
  "status": "success",
  "user": {
    "email": "malomepelumi@gmail.com",
    "name": "Athingban Maulome",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "The first cat show was organized in 1871 in London."
}
```

### Usage Examples:

Test the endpoint using curl:

```bash
curl http://localhost:8000/me
```

Or simply visit in your browser:

```
http://localhost:8000/me
```

## Repository Information

- GitHub Repository: [https://github.com/skyspec28/Hng_stage_0](https://github.com/skyspec28/Hng_stage_0)
- Author: skyspec28
- Email: malomepelumi@gmail.com
