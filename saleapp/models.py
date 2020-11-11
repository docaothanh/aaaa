from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db

class SaleBase(db.Model):
    #Bat co abstract len de csdl khi tao bang nay ma tao 2 bang con cua no
    __abstract__ = True


    id = Column(Integer, primary_key= True, autoincrement=True)
    name = Column(String(50), nullable=False)
    def __str__(self):
        return self.name

class Category(SaleBase):
    __tablename__ = "category"
    products = relationship('Product', backref= 'category',lazy=True)
class Product(SaleBase):
    __tablename__ = "product"
    description = Column(String(255), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id),nullable=False)

if __name__ == "__main__":
    db.create_all()