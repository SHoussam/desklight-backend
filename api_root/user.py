from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.conection import get_session
from database.models.models import User, LoginSchema , SignupSchema
from securety import get_current_user , hash_password , verify_password
import secrets


router = APIRouter()


@router.post("/login/")
def login_user(credentials: LoginSchema, session: Session = Depends(get_session)):
    statement = select(User).where(User.email == credentials.email)
    user = session.exec(statement).first() 
    if not user or not verify_password(credentials.password, user.password):
       raise HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Incorrect email or password"
    )
    return {
        "message": "Login successful",
        "api_key": user.api_key 
    }
@router.get("/user/")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "user_id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
@router.post("/signup/")
def signup_user(nuser: SignupSchema, session: Session = Depends(get_session)):
    s = select(User).where(User.email == nuser.email)
    existing_user = session.exec(s).first()
    if existing_user:     
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    new_api_key = secrets.token_hex(16) 
    hpasseord = hash_password(nuser.password)
    new_user = User(
        name=nuser.name,
        email=nuser.email,
        password=hpasseord,
        api_key=new_api_key
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return {
        "message": "User created successfully", 
        "api_key": new_user.api_key
    }

