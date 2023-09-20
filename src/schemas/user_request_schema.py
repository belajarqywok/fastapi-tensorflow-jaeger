from pydantic import BaseModel

# Register Request Schema
class RegisterRequestSchema(BaseModel) :
    nickname: str
    fullname: str
    birth_date: str

    email: str
    password: str

# Login Request Schema
class LoginRequestSchema(BaseModel) :
    email: str
    password: str


# Refresh Request Schema
class RefreshRequestSchema(BaseModel) :
    refresh_token: str