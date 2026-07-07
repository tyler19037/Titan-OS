from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="CerebrumOS",
    description="AI Personal Operating System",
    version="0.1.0"
)


app.include_router(router)