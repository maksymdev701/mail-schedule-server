from routers import threads
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# create a new FastAPI instance
app = FastAPI()

# define cross origin urls
origins = [
    "http://localhost:3000"
]

# add cors middleware configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(threads.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True, port=9000)
