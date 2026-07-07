from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai_service import generate_response


router = APIRouter()


@router.get("/")
def home():
    return {
        "system": "CerebrumOS",
        "status": "online"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = generate_response(request.message)

    return ChatResponse(
        response=response
    )