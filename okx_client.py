import requests
import json
import hmac
import hashlib
import base64
from urllib.parse import urlparse
from datetime import datetime

HOST = "https://www.okx.com"


class OkxClient:

    def __init__(
        self,
        api_key,
        api_secret,
        api_passphrase,
        is_demo_mode=False
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.is_demo_mode = is_demo_mode
        self.log_tab = "          "

    def get_okx_timestamp(self):
        now = datetime.utcnow()

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        timestamp = now.strftime(date_format)[:-3] + 'Z'

        return timestamp

    def get_body(self, body):
        return json.dumps(body)

    def get_okx_signature(
        self,
        timestamp,
        http_method,
        api_path,
        body
    ):
        message = f"{timestamp}{http_method}{api_path}{body}"

        hmac_hash_string = hmac.new(
            key=self.api_secret.encode('utf-8'),
            msg=message.encode('utf-8'),
            digestmod=hashlib.sha256
        )

        signature = base64.b64encode(
            hmac_hash_string.digest()
        )

        return signature.decode('utf-8')

    def get_headers(
        self,
        http_method,
        api_path,
        body=''
    ):
        timestamp = self.get_okx_timestamp()
        signature = self.get_okx_signature(
            timestamp,
            http_method.upper(),
            api_path,
            body
        )

        headers = {
            "Content-Type": "application/json",
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-SIGN": signature,
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": self.api_passphrase
        }

        if self.is_demo_mode:
            headers["x-simulated-trading"] = "1"

        return headers

    def print_request(self, request):
        method = request.method
        path = urlparse(request.url).path

        print(f"-- REQUEST >>>> ({method}) - {path}")

        body = request.body
        if body is not None:
            print("   >> BODY:")

            json_data = json.loads(body)
            formatted_json = json.dumps(
                json_data,
                indent=2
            )
            for line in formatted_json.splitlines():
                print(f"{self.log_tab}{line}")

        headers = request.headers

        if headers is not None:
            print("\n   >> HEADERS:")

            for key, value in headers.items():
                print(f"{self.log_tab}{key}: {value}")

    def print_response(self, response):
        method = response.request.method
        path = urlparse(response.url).path
        status_code = response.status_code

        print(
            f"\n-- RESPONSE <<<< ({method}) - {path} - {status_code}")
        print("   << HTTP Status:", response.status_code)

        if response.status_code == 200:
            json_data = json.loads(response.text)
            formatted_json = json.dumps(json_data, indent=2)

            print("   << BODY:")

            for line in formatted_json.splitlines():
                print(f"{self.log_tab}{line}")
        else:
            print("Erro ao fazer a requisição:", response.status_code)

        print("\n   << HEADERS:")
        for key, value in response.headers.items():
            print(f"{self.log_tab}{key}: {value}")

        print("\n   << COOKIES:")
        for cookie in response.cookies:
            print(f"{self.log_tab}{cookie.name}: {cookie.value}")

    def get_balance(self):
        endpoint_path = "/api/v5/account/balance"

        headers = self.get_headers(
            http_method="GET",
            api_path=endpoint_path,
            body=""
        )

        response = requests.get(
            url=f"{HOST}{endpoint_path}",
            headers=headers
        )

        self.print_request(response.request)
        self.print_response(response)

    def get_instruments(self, instrument_type="SPOT"):
        endpoint_path = f"/api/v5/public/instruments?instType={instrument_type}"

        headers = self.get_headers(
            http_method="GET",
            api_path=endpoint_path,
            body=""
        )

        response = requests.get(
            url=f"{HOST}{endpoint_path}",
            headers=headers
        )

        self.print_request(response.request)
        self.print_response(response)

    def trade_order_buy(self, instrument_id, amount_string):
        endpoint_path = "/api/v5/trade/order"

        body = {
            "instId": instrument_id,
            "tdMode": "cash",
            "side": "buy",
            "ordType": "market",
            "sz": amount_string
        }

        if self.is_demo_mode:
            body["tt"] = "test"
            body["tag"] = "RTOTestOrder"

        headers = self.get_headers(
            http_method="POST",
            api_path=endpoint_path,
            body=self.get_body(body)
        )

        response = requests.post(
            url=f"{HOST}{endpoint_path}",
            headers=headers,
            data=self.get_body(body)
        )

        self.print_request(response.request)
        self.print_response(response)

    def trade_order_sell(self, instrument_id, amount_string):
        endpoint_path = "/api/v5/trade/order"

        body = {
            "instId": instrument_id,
            "tdMode": "cash",
            "side": "sell",
            "ordType": "market",
            "sz": amount_string
        }

        if self.is_demo_mode:
            body["tt"] = "test"
            body["tag"] = "RTOTestOrder"

        headers = self.get_headers(
            http_method="POST",
            api_path=endpoint_path,
            body=self.get_body(body)
        )

        response = requests.post(
            url=f"{HOST}{endpoint_path}",
            headers=headers,
            data=self.get_body(body)
        )

        self.print_request(response.request)
        self.print_response(response)
