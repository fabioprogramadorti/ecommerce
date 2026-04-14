import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from app.config.settings import settings

class RestClient:

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def send_order(self, order):

        response = requests.post(
            settings.API_URL,
            json={
                "id_pedido": order.id_pedido,
                "cliente": order.cliente,
                "valor": order.valor,
                "status": order.status
            },
            timeout=5
        )

        if response.status_code >= 400:
            raise Exception(f"API error: {response.status_code}")

        return response.json()