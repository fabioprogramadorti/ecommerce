from app.infrastructure.csv.csv_reader import CsvReader

def test_status_transformation():

    reader = CsvReader()

    orders = reader.read("tests/mock_orders.csv")

    statuses = [o.status for o in orders]

    assert "PENDENTE" in statuses
    assert "APROVADO" in statuses
    assert "CANCELADO" in statuses