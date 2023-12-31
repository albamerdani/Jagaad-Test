from fastapi import FastAPI
from app.controller.controller import router

jagaad_app = FastAPI()

jagaad_app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(jagaad_app, host="localhost", port=8000)
