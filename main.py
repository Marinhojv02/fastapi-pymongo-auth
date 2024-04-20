from fastapi import FastAPI
from app.routes.auth_routes import auth_router
app = FastAPI()

app.include_router(auth_router)

@app.get("/health_check", tags=["Root"])
async def health_check():
    return {"message": "Server is working!"}