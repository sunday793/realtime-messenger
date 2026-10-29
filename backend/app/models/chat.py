from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

class ChatMember(Base):
    __tablename__ = "chat_members"

    chat_id = Column(Integer, ForeignKey("chats.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role = Column(String, default="member")