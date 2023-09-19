from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True)
    channel = Column(Integer, default=0)
    numonly = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Guild id={self.id} channel={self.channel} numonly={self.numonly}>"
