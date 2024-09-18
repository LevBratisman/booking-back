from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from app.api.api import main_router
from app.core.config import settings

app = FastAPI()
app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()