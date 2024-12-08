from fastapi import FastAPI
from app.controllers.auth_controller import auth_router
from app.controllers.user_controller import user_router
from app.controllers.product_controller import product_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)

@app.get("/health_check", tags=["Root"])
async def health_check():
    return {"message": "Server is working!"}