from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime

app = FastAPI(title="Profile API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROFILE = {
    "email": "maulomepelumi@gmail.com",
    "name": "Athingban Maulome",
    "stack": "Python/FastAPI"
}

async def fetch_cat_fact():
    """Fetch a random cat fact from the Cat Facts API"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://catfact.ninja/fact", timeout=10.0)
            response.raise_for_status()
            return response.json()["fact"]
        except (httpx.RequestError, KeyError) as e:
            raise HTTPException(
                status_code=503,
                detail="Unable to fetch cat fact. Service temporarily unavailable."
            )

@app.get("/me")
async def get_profile():
    """
    Get profile information along with a random cat fact
    """
    try:
        cat_fact = await fetch_cat_fact()
        return {
            "status": "success",
            "user": PROFILE,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "fact": cat_fact
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
