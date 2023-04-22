from fastapi import APIRouter
from core.database import db

router = APIRouter(prefix="/threads", tags=["threads"])
thread_collection = db["threads"]
document_collection = db["documents"]


@router.get("/", description="Get threads by using pagination")
async def get_threads(page: int = 1, page_size: int = 10):
    # Calculate the number of documents to skip
    skip = (page - 1) * page_size

    # Retrieve the requested page of data
    items = []
    cursor = thread_collection.find().skip(skip).limit(page_size)
    for item in cursor:
        item.pop('_id', None)
        document_collection.find({"data_id"})
        items.append(item)

    return {"items": items, "total": thread_collection.count_documents({})}
