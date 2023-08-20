from models.user import User
from sqlalchemy.orm import Session
from data_transfer_object import user


def get_user(id: int, db: Session):
    return db.query(User).filter(User.id==id).first()


def create_user(data: user.User, db: Session):
    user = User(name=data.name)
    try:
        print(dir(Session))
        db.add(user)
        print("user added?", user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user




