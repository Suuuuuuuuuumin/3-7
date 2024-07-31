from typing import List
from pydantic import BaseModel
#request가 양이 많고 복잡하거나, 연산 후 return 하는 경우가 있기에 response는 다른 파일에서 처리

class userDataSchema(BaseModel):
    userNum: int
    id: str
    pw: str
    email: str
    nickName: str
    
    class Config:
        from_attributes = True
    #pydantic의 orm 모드 사용(), sqlalchemy의 orm객체를 받아 pyadnatic이 사용


class userDataListSchema(BaseModel):
    userData: List[userDataSchema]