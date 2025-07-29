from fastapi import (
    FastAPI,
)

from fastapi.middleware.cors import CORSMiddleware


from .models import Snowflake
from .snowflake import SnowflakeGeneratorBuilder
from .config import settings

builder = SnowflakeGeneratorBuilder()
snowflake_generator = builder.create_generator(node_id=settings.machine_id)
app = FastAPI()

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/", response_model=Snowflake)
async def root():
    id = snowflake_generator()
    return {"id": id}
