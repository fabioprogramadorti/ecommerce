from unittest.mock import Mock
from app.application.use_cases.process_orders import ProcessOrdersUseCase

def test_process_orders_usecase():

    repo = Mock()
    api = Mock()
    logger = Mock()

    orders = [
        Mock(id_pedido=1),
        Mock(id_pedido=2),
        Mock(id_pedido=3)
    ]

    usecase = ProcessOrdersUseCase(repo, api, logger)

    usecase.execute(orders)

    assert api.send_order.call_count == 3
    repo.save_all.assert_called_once()