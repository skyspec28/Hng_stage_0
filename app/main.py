from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Profile API")


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
            logger.info("Fetching cat fact from API")
            response = await client.get("https://catfact.ninja/fact", timeout=10.0)
            response.raise_for_status()
            logger.info("Successfully fetched cat fact")
            return response.json()["fact"]
        except (httpx.RequestError, KeyError) as e:
            logger.error(f"Error fetching cat fact: {str(e)}")
            raise HTTPException(
                status_code=503,
                detail="Unable to fetch cat fact. Service temporarily unavailable."
            )

@app.get("/me")
async def get_profile():
    """
    Get profile information along with a random cat fact
    """
    logger.info("Processing /me endpoint request")
    try:
        cat_fact = await fetch_cat_fact()
        response = {
            "status": "success",
            "user": PROFILE,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "fact": cat_fact
        }
        logger.info("Successfully processed /me endpoint request")
        return response
    except HTTPException as e:
        logger.error(f"HTTP Exception in /me endpoint: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in /me endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
