from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..crud.crud_user import get_user_by_id
from ..models.user import User

def get_current_user(user_id: int, db: Session = Depends(get_db)) -> User:
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user