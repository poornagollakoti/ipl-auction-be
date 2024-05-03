from fastapi import FastAPI
from api.auction_controller import router as auction_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your React frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Mounting controllers
app.include_router(auction_router, prefix="/auction-data")
