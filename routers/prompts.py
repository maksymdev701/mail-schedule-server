from fastapi import APIRouter
from core.database import db

router = APIRouter(prefix="/prompts", tags=["prompts"])
prompt_collection = db["prompts"]


@router.post("/", description="Create new prompt")
async def create_prmopt():
    return {"state": "success"}
