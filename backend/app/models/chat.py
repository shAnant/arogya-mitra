from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class ChatSession(Base):

    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    message = Column(String)

    response = Column(String)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="chat_sessions")