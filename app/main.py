from typing import Optional

from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return "PINGING...."


if __name__ ==  '__main__':
    uvicorn.run(app, port = 8000, host='0.0.0.0')