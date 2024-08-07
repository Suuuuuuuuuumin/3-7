from fastapi.templating import Jinja2Templates
from database.orm import userData
from database.repository import userDataRepository
from fastapi import Body, Depends, Form, HTTPException, Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse

from schema.response import userDataSchema

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/login", response_class=HTMLResponse, status_code=201)
# post    [클라이언트가 서버로 데이터 전송]
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("login.html", {"request": request, "username": username})


@router.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@router.post("/signup", response_class=HTMLResponse, status_code=200)
async def Signup(
    userDataRepo: userDataRepository = Depends(userDataRepository),  #userDataRepository 의존성 주입
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
    savedUserData = userDataRepo.saveUserData(userDataInput=newUserData)
    return str(userDataSchema.from_orm(savedUserData))


@router.get('/userData', status_code=200)
def displayUserData(
    order: str| None = None,  #공란도 실행 가능
    userDataRepo: userDataRepository = Depends(userDataRepository),
):
    userDataList: List[userData] = userDataRepo.getUserData()  # type: ignore 출력값 리스트 형태, userData 테이블 생성 메서드
    if userDataList:
        if order == 'DESC':
            return userDataList[::-1]
        return userDataList
    raise HTTPException(status_code=404, detail = 'UserProfile Not Found')


@router.patch('/userData/{id}', status_code=200)  #유저 아이디로 비밀번호 변경
def updatePwById(
    id: str,
    userDataRepo: userDataRepository = Depends(userDataRepository),
    newPw: str = Body(...)
    ) -> userDataSchema:
    foundUserData : userData | None = userDataRepo.getUserDataById(id = id) # type: ignore
    if foundUserData:
        newUserData: userData = foundUserData.updatePw(newPw = newPw)
        savedUserData: userData = userDataRepo.updateUserData(userDataInput=newUserData)
        return userDataSchema.from_orm(savedUserData)
    raise HTTPException(status_code=404, detail = 'UserProfile Not Found')


@router.delete('/userData/del/{id}', status_code=204)   #유저 회원탈퇴 기능
def deleteUserDataById(
    id = str,
    userDataRepo: userDataRepository = Depends(userDataRepository)
    ):
    foundUserData : userData | None = userDataRepo.getUserDataById(id = id) # type: ignore
    if foundUserData:
        userDataRepo.deleteUserData(deleteId=id)
        return  # Return a 204 No Content response
    raise HTTPException(status_code=404, detail = 'UserProfile Not Found')