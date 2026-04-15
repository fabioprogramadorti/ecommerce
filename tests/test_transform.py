from app.infrastructure.csv.csv_reader import CsvReader

def test_status_transformation():

    reader = CsvReader()

    orders = reader.read("tests/mock_orders.csv")

    assert len(orders) > 0

    statuses = {o.status for o in orders}

    valid_statuses = {"PENDENTE", "APROVADO", "CANCELADO"}
    
    assert statuses.issubset(valid_statuses)