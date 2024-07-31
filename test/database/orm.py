from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from schema.request import createUserDataRequset
#데이터 베이스 테이블을 파이썬에서 직접 매핑, python을 통해 데이터베이스 매핑

base = declarative_base()

class userData(base):
#userProfile이라는 table 생성하기 위한 클래스
    __tablename__ = 'userData'
    #database의 userProfile data에 mapping
    
    userNum = Column(Integer, primary_key=True, autoincrement= True, nullable=False)
    #테이블 열, 프라이머리 키 자동 증가
    id = Column(String(256), nullable=False)
    pw = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    nickName = Column(String(256), nullable=False)

    def __repr__(self):
        return f'loginInfo(userNum={self.userNum}, id={self.id}, pw={self.pw}, email={self.email}, nickName={self.nickName})'
    
    @classmethod
    def createUserData(cls, request: createUserDataRequset) -> 'userData':
        return cls(
            id = request.id,
            pw = request.pw,
            email = request.email,
            nickName = request.nickName
        )
