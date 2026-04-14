from sqlalchemy import text
from app.infrastructure.database.connection import SessionLocal
from app.infrastructure.database.models import OrderModel


class PostgresRepository:

    def __init__(self):
        self.db = SessionLocal()

    
    def save(self, order):
        try:
            db_order = OrderModel(
                id_pedido=order.id_pedido,
                cliente=order.cliente,
                valor=order.valor,
                status=order.status
            )

            self.db.add(db_order)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise e

    
    def save_all(self, orders):
        try:
            db_orders = [
                OrderModel(
                    id_pedido=o.id_pedido,
                    cliente=o.cliente,
                    valor=o.valor,
                    status=o.status
                )
                for o in orders
            ]

            self.db.bulk_save_objects(db_orders)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise e

    
    def get_report_data(self):
        try:
            query = text("""
                SELECT 
                    status,
                    COUNT(*) as total_pedidos,
                    SUM(valor) as valor_total
                FROM orders
                GROUP BY status
            """)

            result = self.db.execute(query).fetchall()
            return result

        except Exception as e:
            raise e

    
    def close(self):
        self.db.close()