from fastapi import (
    FastAPI,
)


from .models import Snowflake
from .snowflake import SnowflakeGeneratorBuilder
from .config import settings

builder = SnowflakeGeneratorBuilder()
snowflake_generator = builder.create_generator(node_id=settings.machine_id)
app = FastAPI()


@app.get("/", response_model=Snowflake)
async def root():
    id = snowflake_generator()
    return {"id": id}
