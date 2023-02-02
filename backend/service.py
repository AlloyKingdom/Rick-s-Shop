from models.shoes_model import ShoesModel
from schemas.shoes_schema import Shoes, UpdateShoesRequest
from sqlalchemy.orm import Session


# 取得全部鞋子
def get_all_shoes(db: Session):

    """
    Return a list of all existing Shoes records
    """

    all_shoes = db.query(ShoesModel).all()

    items = []
    for item in all_shoes:
        items.append(item)
    print(len(items))
    return all_shoes


# 增加一款鞋子
def create_shoes(db: Session, request: Shoes):

    """
    function to create a shoes model object
    """

    all_shoes = get_all_shoes(db)
    items = []
    for item in all_shoes:
        items.append(item)
    
    new_shoes = ShoesModel(
        id=len(items)+1,
        volume_id=request.volume_id,
        name=request.name,
        brand=request.brand,
        thumbnail=request.thumbnail,
        style=request.style,
        state=request.state,
        price=request.price,
        sale_price=request.sale_price,
        detail=request.detail
    )
    db.add(new_shoes)
    db.commit()
    db.refresh(new_shoes)
    return new_shoes


# 取得一双鞋子 by 货号
def get_one_shoes(db: Session, volume_id: str):

    """
    get the first record with a given id, if no such record exists, will return null
    """

    shoes = db.query(ShoesModel).filter(ShoesModel.volume_id==volume_id).first()
    return shoes


# 更新一双鞋子
def update_shoes(db: Session, volume_id: str, request: UpdateShoesRequest):

    """
    Update a product of shoes' information
    """

    shoes = get_one_shoes(db=db, volume_id=volume_id)
    shoes.name = request.name
    shoes.brand = request.brand
    shoes.thumbnail = request.thumbnail
    shoes.style = request.style
    shoes.state = request.state
    shoes.price = request.price
    shoes.sale_price = request.sale_price
    shoes.detail = request.detail
 
    db.commit()
    db.refresh(shoes)
    return shoes


# 删除一双鞋子
def delete_shoes(db: Session, volume_id: str):

    """
    Delete a product of shoes
    """

    db_friend = get_one_shoes(db=db, volume_id=volume_id)
    db.delete(db_friend)
    db.commit()


# app = FastAPI(debug=True)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Hello
# @app.get("/status")
# async def check_status():
#     return "I'm Pickle Rick!"

# # connect to our database
# conn = psycopg2.connect(
#         database="rick_shop", user="postgres", password="user", host="localhost", port=5432
#     )


# # 取得全部鞋子
# @app.get("/shoes", response_model=List[Shoes], status_code=status.HTTP_200_OK)
# async def get_all_shoes():
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM shoes ORDER BY id DESC")
#     rows = cur.fetchall()

#     formatted_shoes = []
#     for row in rows:
#         formatted_shoes.append(
#             Shoes(
#                 id=row[0],
#                 volume_id=row[1],
#                 name=row[2],
#                 brand=row[3],
#                 thumbnail=row[4],
#                 style=row[5],
#                 state=row[6],
#                 price=row[7],
#                 sale_price=row[8],
#                 detail=row[9],
#             )
#         )
#     cur.close()
#     conn.close()

#     return formatted_shoes


# # 增加一款鞋子
# @app.post("/shoes", status_code=status.HTTP_201_CREATED)
# async def create_shoes(shoes: Shoes):
#     cur = conn.cursor()
#     cur.execute(f"INSERT INTO shoes (volume_id, name, brand, thumbnail, style, state, price, sale_price, detail) VALUES ('{shoes.volume_id}', '{shoes.name}', '{shoes.brand}', '{shoes.thumbnail}', '{shoes.style}', '{shoes.state}', '{shoes.price}', '{shoes.sale_price}' ,'{shoes.detail}')")

#     cur.close()
#     conn.commit()
#     conn.close()

#     return shoes

# # 展示
# @app.get("/show/{volume_id}")
# async def show(shoes: Shoes):
#     cur = conn.cursor()
#     cur.execute(f"SELECT thumbnail FROM shoes WHERE volume_id = '{shoes.volume_id}'")
#     cur.close()
#     conn.commit()
#     conn.close()
#     image = shoes.thumbnail
#     return FileResponse("https://img.ssensemedia.com/images/b_white,c_lpad,g_south,h_706,w_470/c_scale,h_280/f_auto,dpr_1.0/222378M228002_1/ann-demeulemeester-black-mick-boots.jpg")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
