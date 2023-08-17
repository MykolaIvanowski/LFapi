from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": {"say hi": "Five years latter Hello World!!!"} }