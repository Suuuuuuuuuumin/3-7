from sqlalchemy import create_engine
#engine은 sqlalchemy 적용, 데이터베이스 연결 설정을 책임지는 인터페이스
from sqlalchemy.orm import sessionmaker
#sessionmaker 함수, 데이터베이스 세션 생성

DATABASE_URL = 'mysql+pymysql://root:ytjeong02!@127.0.0.1:3307/userData'    
#데이터베이스에 연결하기 위한 url 정의, root계정,userProfile비번,포트 주소, userProfile 데이터베이스

engine = create_engine(DATABASE_URL, echo = True)
#데이터 베이스 엔진 생성, echo 디버깅을 위해 SQLAlchemy의 모든 sql문 출력, 엔진이라는 객체가 있어야 데이터베이스 접속 가능

sessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#변경 사항 저장을 위해 자동 동작 방지, 수동 조작, engine을 통해서 session을 만들 수 있게 됨, session이란 데이터베이스와 교신하기 위한 임시의 가상 환경, 이를 통해 query 동작

def getDB():
#python generator, 세션(session lifecycle) 관리, 의존성 주입
    session = sessionFactory()
    try:
        yield session
    finally:
        session.close()