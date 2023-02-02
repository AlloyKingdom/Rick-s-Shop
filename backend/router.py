import service
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.shoes_schema import CreateShoesRequest, UpdateShoesRequest
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, FileResponse


router = APIRouter()

# 增加一款鞋子
@router.post("/create_shoes", tags=["Shoes"])
def create_shoes(request: CreateShoesRequest, db: Session = Depends(get_db)):
    shoes = service.create_shoes(db=db, request=request)
    return {"New Shoes": shoes}
 

# 取得全部鞋子
@router.get("/list_shoes", tags=["Shoes"])
def get_all_shoes(db: Session = Depends(get_db)):
    shoes_list = service.get_all_shoes(db=db)
    return shoes_list
 

# 取得一双鞋子 by 货号
@router.get("/get_shoes/{volume_id}/", tags=["Shoes"])  # id is a path parameter
def get_one_shoes(volume_id: str, db: Session = Depends(get_db)):
    shoes = service.get_one_shoes(db=db, volume_id=volume_id)
    return shoes


# 更新一双鞋子 
@router.put("/update_shoes/{volume_id}/", tags=["Shoes"])  # id is a path parameter
def update_shoes(request: UpdateShoesRequest, db: Session = Depends(get_db)):
    # get shoes object from Session
    db_shoes = service.get_one_shoes(db=db, id=id)
    # check if shoes object exists
    if db_shoes:
        updated_shoes = service.update_shoes(db=db, request=request)
        return updated_shoes
    else:
        return {"error": f"shoes with volume_id {request.volume_id} does not exist"}


# 删除一双鞋子
@router.delete("/delete_shoes/{volume_id}/", tags=["Shoes"])  # id is a path parameter
def delete_shoes(volume_id: str, db: Session = Depends(get_db)):
    # get shoes object from Session
    db_shoes = service.get_one_shoes(db=db, volume_id=volume_id)
    # check if shoes object exists
    if db_shoes:
        return service.delete_shoes(db=db, volume_id=volume_id)
    else:
        return {"error": f"shoes with volume_id {volume_id} does not exist"}


# 取得商店图片
@router.get("/show_img/", response_class=HTMLResponse)  # id is a path parameter
def show_image(db: Session = Depends(get_db)):
    return FileResponse("Rick_Sanchez_Fortnite.png")
