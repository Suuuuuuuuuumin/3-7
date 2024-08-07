from typing import List
from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from database.connection import getDB
from database.orm import userData

class userDataRepository:
    def __init__(self, session: Session= Depends(getDB)):
        self.session = session

    def getUserData(self) -> List[userData]:
        #->List[userProfile]: 출력값 형태 알려줌
        return list(self.session.scalars(select(userData)))

    def getUserDataById(self, id: int):
        return self.session.scalar(select(userData).where(userData.id==id))

    def saveUserData(self, userDataInput: userData)->userData:
        self.session.add(instance=userDataInput)   #추가할 데이터를 session객체에 축적
        self.session.commit()   #데이터베이스에 실제로 추가
        self.session.refresh(instance=userDataInput)   #데이터베이스를 새로고침(return을 위해서)
        return userDataInput

    def updateUserData(self, userDataInput: userData)->userData:
        self.session.add(instance=userDataInput)   #추가할 데이터를 session객체에 축적
        self.session.commit()   #데이터베이스에 실제로 추가
        self.session.refresh(instance=userDataInput)   #데이터베이스를 새로고침(return을 위해서)
        return userDataInput

    def deleteUserData(self, deleteId: str)->None:
        self.session.execute(delete(userData).where (userData.id == deleteId))
        self.session.commit()