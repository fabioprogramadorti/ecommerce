import csv
from app.domain.dtos.order_dto import OrderDTO

STATUS_MAP = {    
    "PENDING": "PENDENTE",
    "PENDENTE": "PENDENTE",
    "HANDLING": "PENDENTE",    
    "APPROVED": "APROVADO",
    "APROVADO": "APROVADO",    
    "CANCELED": "CANCELADO",
    "CANCELLED": "CANCELADO",
    "CANCELADO": "CANCELADO",    
    "ESTORNADO": "CANCELADO",
}


class CsvReader:

    def read(self, file_path: str, limit: int = None):
        orders = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:

            sample = csvfile.read(1024)
            csvfile.seek(0)

            try:
                dialect = csv.Sniffer().sniff(sample)
                reader = csv.DictReader(csvfile, dialect=dialect)
            except Exception:
                reader = csv.DictReader(csvfile)

            for i, row in enumerate(reader):

                if limit is not None and i >= limit:
                    break

                if not any(row.values()):
                    continue

                
                id_pedido = str(row.get("id_pedido") or "").strip()
                cliente = str(row.get("cliente") or "").strip()
                valor = str(row.get("valor") or "").strip()

                if not id_pedido or not cliente:
                    continue

                
                status_raw = str(
                    row.get("status") or row.get("status_pagamento") or ""
                ).strip().upper()

                status = STATUS_MAP.get(status_raw)

                
                if not status:
                    print(f"[WARN] Status ignorado: '{status_raw}' | Linha: {row}")
                    continue

                try:
                    order = OrderDTO(
                        id_pedido=int(id_pedido),
                        cliente=cliente,
                        valor=float(valor),
                        status=status
                    )
                except (ValueError, TypeError):
                    print(f"[WARN] Erro ao converter linha: {row}")
                    continue

                orders.append(order)

        return orders