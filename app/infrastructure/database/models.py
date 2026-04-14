from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

Base = declarative_base()

class OrderModel(Base):
    __tablename__ = "orders"

    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True)
    cliente: Mapped[str] = mapped_column(String)
    valor: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String)
