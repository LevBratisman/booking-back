from fastapi import FastAPI
import uvicorn

from app.api.api import main_router

app = FastAPI()
app.include_router(main_router)


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()