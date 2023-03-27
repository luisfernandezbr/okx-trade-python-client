from okx_client import OkxClient
from dotenv import load_dotenv
import os
from okx_runner import OkxRunner

okx_runner = OkxRunner()
okx_client = okx_runner.okx_client


def run(action):
    match action:
        case "get_instruments":
            okx_client.get_instruments(instrument_type="SPOT")
        case "get_balance":
            okx_client.get_balance()
        case "trade_buy":
            okx_client.trade_order_buy(
                instrument_id="BTC-USDT",
                amount_string="0.2797"
            )
        case "trade_sell":
            okx_client.trade_order_sell(
                instrument_id="BTC-USDT",
                amount_string="0.00001"
            )
        case _:
            print("Invalid input")


# run("get_instruments")
# run("get_balance")
run("trade_buy")
# run("trade_sell")
