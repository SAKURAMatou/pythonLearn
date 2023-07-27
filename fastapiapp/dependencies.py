from fastapi import Header, HTTPException


async def get_token_headers(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str = Header()):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


class MyException(Exception):
    def __init__(self, des: str):
        self.des = des