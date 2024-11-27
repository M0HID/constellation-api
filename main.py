from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {
        "city": "London",
        "state": "N/A",
        "country": "UK",
        "slack_id": "U07FC2JPHMX",
        "extra": "hi alex"
    }