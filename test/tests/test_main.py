from fastapi.testclient import TestClient
from main import router

client = TestClient(app=router)

#전체 userData 조회
def testGetUserData():
    response = client.get("/userData")
    assert response.status_code == 200
    assert response.json() == [
    {
    "userNum": 1,
    "id": "정민우",
    "pw": "ytjeong02!",
    "email": "tonyjeong02@gmail.com",
    "nickName": "ytjeong02!"}]


#전체 userData 조회, oreder = DESC
def testGetUserDataDESC():
    response = client.get("/userData?order=DESC")
    assert response.status_code == 200
    assert response.json() == [
    {
    "userNum": 1,
    "id": "정민우",
    "pw": "ytjeong02!",
    "email": "tonyjeong02@gmail.com",
    "nickName": "ytjeong02!"}]