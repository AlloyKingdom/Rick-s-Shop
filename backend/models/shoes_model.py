from sqlalchemy import Column, Integer, String
 
from db.base import Base
 
# model/table
class ShoesModel(Base):
    __tablename__ = "shoes"
 
    # fields
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    volume_id = Column(String(15), nullable=False)
    name = Column(String(50))
    brand = Column(String(50))
    thumbnail = Column(String(255))
    style = Column(String(255))
    state = Column(String(6))
    price = Column(Integer)
    sale_price = Column(Integer)
    detail = Column(String(255))
