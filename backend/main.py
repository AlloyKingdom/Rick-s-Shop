from fastapi import FastAPI
from apis.general_pages.route_homepage import general_pages_router
from router import router


app = FastAPI()
app.include_router(router)

# define endpoint
# http://lcoalhost:8000/（返回 {"I'm Pickle Rick!"}）
# http://lcoalhost:8000/docs 自动交互式 API 文档（SwaggerUI）
@app.get("/")
def home():
    return {"I'm Pickle Rick!"}

# uvicorn main:app --reload
