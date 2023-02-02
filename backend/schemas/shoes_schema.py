from pydantic import BaseModel


class Shoes(BaseModel):     # 鞋子
    id: int                 # id
    volume_id: str          # 编号
    name: str               # 名字
    brand: str              # 品牌
    thumbnail: str          # 缩略图
    style: str              # 款式
    state: str              # 状态
    price: int              # 价格
    sale_price: int         # 折后价
    detail: str             # 细节

    class Config:
        orm_mode = True


class CreateShoesRequest(BaseModel):     # 增加鞋子
    volume_id: str          # 编号
    name: str               # 名字
    brand: str              # 品牌
    thumbnail: str          # 缩略图
    style: str              # 款式
    state: str              # 状态
    price: int              # 价格
    sale_price: int         # 折后价
    detail: str             # 细节


class UpdateShoesRequest(BaseModel):     # 更新鞋子
    name: str               # 名字
    brand: str              # 品牌
    thumbnail: str          # 缩略图
    style: str              # 款式
    state: str              # 状态
    price: int              # 价格
    sale_price: int         # 折后价
    detail: str             # 细节

