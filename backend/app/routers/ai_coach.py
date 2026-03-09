from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.chat import ChatRequest
from app.models.chat import ChatSession
from app.services.ai_agent import ArogyaMitraAgent
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/aromi", tags=["AROMI AI Coach"])

agent = ArogyaMitraAgent()


@router.post("/chat")

async def aromi_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    history = db.query(ChatSession).filter(
        ChatSession.user_id == user.id
    ).order_by(ChatSession.created_at.desc()).limit(5).all()

    ai_response = await agent.aromi_coach(
        user,
        request.message,
        history
    )

    chat = ChatSession(
        user_id=user.id,
        message=request.message,
        response=ai_response
    )

    db.add(chat)
    db.commit()

    return {"response": ai_response}