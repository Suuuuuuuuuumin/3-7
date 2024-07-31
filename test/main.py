from fastapi import Depends, FastAPI, Form, HTTPException, Request
# FastAPI    [FastAPI 어플리케이션 생성]
# Form    [Form 데이터 수집]
# Request    [요청 객체]
from fastapi.responses import HTMLResponse, RedirectResponse
# HTMLResponse   [HTML 콘텐츠 반환]
# RedirectResponse   [리디엑션]
from fastapi.templating import Jinja2Templates
# Jinja2Templates    [Jinja2 템플릿 사용(Python 기반으로 Html 파일 동적 생성)]

from sqlalchemy.orm import Session
from database.repository import getUserData, saveUserData
from database.connection import getDB
from database.orm import userData
from schema.request import createUserDataRequset
from schema.response import userDataListSchema, userDataSchema
# CSV    [CSV 형식의 파일 권한(rwd)]

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# app = FastAPI()    [FastAP 어플리케이션 인스턴스 생성]
# Jinja2Templates(directory="templates")    [Jinja2 템플릿 지정]

UsersData = "UsersData.csv"
# "UsersData.csv"    [사용자 정보 저장 경로]

'''def SaveUsersToCSV(username:str, nickname:str, password:str, email:str):
    with open(UsersData, mode='a', newline='') as file:
    # mode='a'    [추가모드'a']
    # newline=''    [줄바꿈 문제 방지]
        writer = csv.writer(file)
        # [CSV 작성기 객체 생성]
        writer.writerow([username, nickname, password, email])
        # ['[]'형식으로 작성]'''



@app.get("/", response_class=HTMLResponse, status_code=200)
# get    [요청 사항 랜더링]
# "/"    "/"[루트 URL/"에서 호출]
# response_class=HTMLResponse    [응답을 HTML 형식으로 반환]
async def ReadRoot(request: Request):
# async def    [비동기 함수]
# : Request    [request라는 매게 변수가 FastAPI의 'Request' 타입]
    return templates.TemplateResponse("login.html", {"request": request})
    # TemplatesResponse    [Jinja2 템플릿을 활용하여 HTML 응답을 생성하는 FastAPI의 클래스]
    # {}    [탬플릿에 전달할 컨텍스트 데이터]



@app.post("/login", response_class=HTMLResponse, status_code=200)
# post    [클라이언트가 서버로 데이터 전송]
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("login.html", {"request": request, "username": username})


@app.post("/signup", response_class=HTMLResponse, status_code=200)
async def SignupForm(
    session: Session = Depends(getDB),
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    nickname: str = Form(...)    
    ):
    newUserData =userData(
            id=username,
            pw=password,
            email=email,
            nickName=nickname
        )
    savedUserData: userData = saveUserData(session=session, userDataInput=newUserData)
    userDataDict = {
        "userNum": int(savedUserData.userNum),
        "id": str(savedUserData.id),
        "pw": str(savedUserData.pw),
        "email": str(savedUserData.email),
        "nickName": str(savedUserData.nickName)
    }
    return userDataSchema.model_validate(userDataDict)



@app.get('/userData', status_code=200)
def displayUserData(
    order: str| None = None,  #공란도 실행 가능
    session: Session = Depends(getDB)  #session 의존성 주입
):
    userDataList: List[userData] = getUserData(session=session)  # type: ignore 출력값 리스트 형태, userProfile 테이블 생성 메서드
    if userDataList:
        return userDataList
    raise HTTPException(status_code=404, detail = 'UserProfile Not Found')