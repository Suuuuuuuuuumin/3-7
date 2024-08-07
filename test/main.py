from fastapi import FastAPI, Request
# FastAPI    [FastAPI 어플리케이션 생성]
# Form    [Form 데이터 수집]
# Request    [요청 객체]
from fastapi.responses import HTMLResponse
from api import account
# HTMLResponse   [HTML 콘텐츠 반환]
# RedirectResponse   [리디엑션]
from fastapi.templating import Jinja2Templates
# Jinja2Templates    [Jinja2 템플릿 사용(Python 기반으로 Html 파일 동적 생성)]


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(account.router) 
Jinja2Templates(directory="templates")   # [Jinja2 템플릿 지정]


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



