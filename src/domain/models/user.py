from sqlalchemy import Column, String

from src.common.database import Base


class UserModel(Base):
    name = Column(String(50), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String(255), nullable=False)
