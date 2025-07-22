from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import os

app = FastAPI(title="Recruto test")

@app.get("/", response_class=PlainTextResponse)
async def greet(
    name: str = Query(..., description="Имя / компания"),
    message: str = Query(..., description="Приветственное сообщение"),
):
    return f"Hello {name}! {message}!"

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
