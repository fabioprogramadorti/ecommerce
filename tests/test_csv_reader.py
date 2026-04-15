from app.infrastructure.csv.csv_reader import CsvReader

def test_csv_reader_loads_data():

    reader = CsvReader()

    orders = reader.read("tests/mock_orders.csv")

    assert len(orders) > 0

    for order in orders:
        assert order.id_pedido is not None
        assert order.cliente is not None
        assert order.valor is not None
        assert order.status in ["PENDENTE", "APROVADO", "CANCELADO"]