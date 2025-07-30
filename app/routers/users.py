
from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse
from app.schemas import UserCreate, UserRead

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, background_tasks: BackgroundTasks):
    # Register user logic (database interaction)
    # Trigger background task for sending welcome email here
    return JSONResponse(content={}, status_code=201)
