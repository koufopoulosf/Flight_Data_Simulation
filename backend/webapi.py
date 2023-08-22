from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
import asyncpg, uvicorn, os

app = FastAPI(
    title="Flight Data Simulator",
    description="Data Project!",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    load_dotenv()
    credentials = {
        "user": os.getenv("pg_user"),
        "password": os.getenv("pg_password"),
        "database": os.getenv("pg_database"),
        "host": os.getenv("pg_host"),
        "port": os.getenv("pg_port")
    }
    app.connection_pool = await asyncpg.create_pool(**credentials)

@app.on_event("shutdown")
async def shutdown():
    await app.connection_pool.close()

@app.get('/v1/planes', tags=['Planes'])
async def get_planes():
    async with app.connection_pool.acquire() as conn: # PG Pooling
        return ORJSONResponse(content=[dict(row) for row in await conn.fetch("SELECT id, lat::text, long::text FROM flight_data ORDER BY id;")])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)