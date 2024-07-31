from pydantic import BaseModel

class createUserDataRequset(BaseModel):
    id: str
    pw: str
    email: str
    nickName: str
    #basemodel을 상속 받아서 각 아이템 속성 설정, 적합한 request body 판별, 해당 클래스에서 request body 선택 가능