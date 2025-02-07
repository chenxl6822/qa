from fastapi import FastAPI, Body
from fastapi.params import Param
from pydantic import BaseModel

app = FastAPI()


class CommonResponse(BaseModel):
    code: int
    message: str
    data: object


valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"


class User(BaseModel):
    username: str
    nickname: str
    email: str


user = User(
    username="testuser",
    nickname="测试用户",
    email="testuser@example.com")


@app.post("/api/login")
async def login(username: str = Body(), password: str = Body()):
    if username == "admin" and password == "admin":
        return CommonResponse(code=200, message="登录成功", data={
            "token": valid_token
        })
    else:
        return CommonResponse(code=400, message="登录失败", data=None)


@app.get("/api/user/info")
async def get_info(token: str = Param()):
    if token == valid_token:
        return CommonResponse(code=200, message="获取成功", data=user)
    else:
        return CommonResponse(code=401, message="身份验证失败", data=None)
