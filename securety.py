from fastapi import Security, HTTPException, status , Depends
from fastapi.security import APIKeyHeader
from sqlmodel import Session, select
from database.conection import get_session
from database.models.models import User
import bcrypt

# hash password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# 1. Define the exact name of the header the frontend will send
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

# 2. Create the security function
def get_current_user(
    api_key: str = Security(api_key_header), 
    session: Session = Depends(get_session)
):
    # Check if the header was sent at all
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing x-api-key header"
        )
    

    statement = select(User).where(User.api_key == api_key)
    user = session.exec(statement).first()
    
    # If the key doesn't match anyone in the database, reject them
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
        
    # If everything is good, hand the user object to the endpoint
    return user

