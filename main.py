import uvicorn

from fastapi import FastAPI
from db_connection import Base, session_local, engine
from routers import user as user_router


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router.router, prefix="/user")


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8008, reload=True, workers=4)


