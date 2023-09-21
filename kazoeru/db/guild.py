from sqlalchemy import BigInteger, Boolean, Column

from kazoeru.db.base import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(BigInteger, primary_key=True)
    channel = Column(BigInteger, default=0)
    numonly = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Guild id={self.id} channel={self.channel} numonly={self.numonly}>"
