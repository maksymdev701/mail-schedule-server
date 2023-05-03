from fastapi import APIRouter
from core.database import db, put_documents, load_threads
from bson.objectid import ObjectId

router = APIRouter(prefix="/threads", tags=["threads"])
thread_collection = db["threads"]
document_collection = db["documents"]

@router.get("/load", description="Load threads from json file")
async def load():
    load_threads()
    return {"message": "Successfully loaded threads from json file"}

@router.get("/", description="Get threads by using pagination")
async def get_all_threads(page: int = 1, page_size: int = 10):
    # Calculate the number of documents to skip
    skip = (page - 1) * page_size

    # Retrieve the requested page of data
    items = []
    cursor = thread_collection.find().skip(skip).limit(page_size)
    for item in cursor:
        item.pop('_id', None)
        items.append(item)

    return {"items": items, "total": thread_collection.count_documents({})}


@router.get("/{id}", description="Get thread by using id")
async def get_thread_by_id(id: str):
    doc_count = document_collection.count_documents(
        {"thread_id": ObjectId(id)})
    thread = thread_collection.find_one({"_id": id})
    if doc_count == 0:
        put_documents()
    return {"docs": {}}
