"""
Main file
"""
import time
import asyncio
import uvicorn

from fastapi import FastAPI
from db_config import create_tables

from routers import user, system


import secrets

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"


DESCRIPTION = """
Ax Technology API helps you do awesome stuff. 🚀

## Users CRUD and List via APIs

You can: 
- create user
- read user
- update user
- delete user
- see user list
"""

app = FastAPI(
    title="Ax Technology test",
    version="1.0.0",
    description=DESCRIPTION,
    contact={
        "name": "Tatibaev Murat",
        "email": "tatibaevmurod@gmail.com",
    },
    openapi_url="/api/v1/openapi.json",
)


app.include_router(system.router)
app.include_router(user.router)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(create_tables())
    end = time.time()
    print("Time elapsed: ", end - start)

    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)
