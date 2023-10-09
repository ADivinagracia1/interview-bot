from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("beepoboop")
    return {"message": "Hello World"}
