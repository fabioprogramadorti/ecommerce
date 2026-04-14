import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from app.config.settings import settings

class RestClient:

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def send_order(self, order):
        r = requests.post(settings.API_URL, json=order.__dict__, timeout=5)
        if r.status_code >= 400:
            raise Exception("API error")
