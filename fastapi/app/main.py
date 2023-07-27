import uvicorn
from fastapi import FastAPI, Depends
from .dependencies import get_token_headers, get_query_token
from .routers import items, users
from .internal import admin

# items和users中都有相同的变量名router，为了避免冲突，通过模块.变量名方式引用

# include_router把 APIRouter 添加到主 FastAPI 应用程序中。
app = FastAPI(debug=True, dependencies=[Depends(get_query_token)])
# 在app中使用子模块中的接口
app.include_router(users.router)
app.include_router(items.router)

# 假设admin中的接口时无法被修改的，想要添加项目已有的dependencies，以及接口路径前缀可以把相关信息通过app.include_router()配置
app.include_router(admin.router,
                   prefix="/admin",
                   dependencies=[Depends(get_query_token)],
                   responses={418: {"description": "I'm a teapot"}}, )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
