from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import openai
import os

from app.routers.pdf_router import pdf_router

app = FastAPI()


# Debugging CORS middleware
try:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows CORS from this origin
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
    print("CORS middleware added successfully for development environment")
except Exception as e:
    print(f"Error adding CORS middleware: {e}")

# Debugging router inclusion
try:
    app.include_router(pdf_router)
    print("Routers included successfully")
except Exception as e:
    print(f"Error including routers: {e}")