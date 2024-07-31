from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.orm import userData

def getUserData(session: Session) -> List[userData]:
    #->List[userProfile]: 출력값 형태 알려줌
    return list(session.scalars(select(userData)))

def getUserDataByUserNum(session: Session, userNum: str):
    return session.scalar(select(userData).where(userData.userNum==userNum))

def saveUserData(session: Session, userDataInput: userData)->userData:
    session.add(instance=userDataInput)   #추가할 데이터를 session객체에 축적
    session.commit()   #데이터베이스에 실제로 추가
    session.refresh(instance=userDataInput)   #데이터베이스를 새로고침(return을 위해서)
    return userData