import csv
from app.domain.dtos.order_dto import OrderDTO

STATUS_MAP = {
    "PENDENTE": "PENDENTE",
    "APROVADO": "APROVADO",
    "CANCELADO": "CANCELADO",
    "ESTORNADO": "CANCELADO",
}

class CsvReader:

    def read(self, file_path: str, limit: int = None):
        orders = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for i, row in enumerate(reader):

                if limit is not None and i >= limit:
                    break

                if not any(row.values()):
                    continue

                if not row.get("id_pedido") or not row.get("cliente"):
                    continue

                status_raw = (
                    row.get("status")
                    or row.get("status_pagamento")
                    or ""
                ).strip().upper()

                status = STATUS_MAP.get(status_raw)

                if not status:
                    continue

                try:
                    order = OrderDTO(
                        id_pedido=int(row["id_pedido"]),
                        cliente=row["cliente"].strip(),
                        valor=float(row["valor"]),
                        status=status
                    )
                except (ValueError, TypeError):
                    continue

                orders.append(order)

        return orders