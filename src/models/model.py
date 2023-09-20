import uuid
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, String, Date, ForeignKey
from src.configurations.databases.postgresql import Base


"""
User (table=users):
 - id: String, Primary Key, Surrogate Key
 - nickname: String(16)
 - fullname: String(64)
 - birthdate: Date
 - createdAt: Date
 - updatedAt: Date

 Indexing: id, nickname
"""
class User(Base):
    __tablename__: str = 'users'

    id: Mapped[String] = Column(
        String,
        primary_key = True,
        default = str(uuid.uuid4()),
        index = True
    )

    nickname: Mapped[String] = Column(String(16), index = True)
    fullname: Mapped[String] = Column(String(64))

    birthdate: Mapped[Date] = Column(Date) 
    createdAt: Mapped[Date] = Column(Date)
    updatedAt: Mapped[Date] = Column(Date)

    credential: Mapped[object] = relationship(
        'Credential',
        back_populates = 'owner',
        uselist = False
    )



"""
Credential (table=credentials):
 - id: String, Primary Key, Surrogate Key
 - email: String(32), Unique
 - password: String(128)
 - user_id: String, Unique

 Indexing : id, email
"""
class Credential(Base):
    __tablename__: str = 'credentials'

    id: Mapped[String] = Column(
        String,
        primary_key = True,
        default = str(uuid.uuid4()),
        index = True
    )

    email: Mapped[String] = Column(String(32), index = True, unique = True)
    password: Mapped[String] = Column(String(128))

    owner_id: Mapped[String] = Column(String, ForeignKey('users.id'), unique = True)
    owner: Mapped[object] = relationship(
        'User',
        back_populates = 'credential',
        uselist = False
    )