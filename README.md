# okx-trade-python-client

This is a project to test OKX API

You need to create a .env file on the project's root folder with the following content:

```
# CHOOSE PRODUCTION or DEMO
ENVIRONMENT=DEMO

# DEMO
DEMO_API_KEY=THE_CONTENT_OF_YOUR_DEMO_API_KEY_HERE
DEMO_API_SECRET=THE_CONTENT_OF_YOUR_DEMO_API_SECRET_HERE
DEMO_API_PASSPHRASE=THE_CONTENT_OF_YOUR_DEMO_API_PASSPHRASE_HERE

# PRODUCTION
API_KEY=THE_CONTENT_OF_YOUR_API_KEY_HERE
API_SECRET=THE_CONTENT_OF_YOUR_API_SECRET_HERE
API_PASSPHRASE=THE_CONTENT_OF_YOUR_API_PASSPHRASE_HERE
```

An example here. ; )
https://gist.github.com/luisfernandezbr/9216bfbed9ea5f67a9d464f52db6f9ca#file-env


See more about here PRODUCTION and DEMO environments at:
https://www.okx.com/docs-v5/en/#overview-v5-api-key-creation


Pay Attention.
To do trading, you need to have funds on trading account.
Add funds and transfer from funding account.

To run, choose on off the options on main.py file:
```
run("get_instruments")
run("get_balance")
run("trade_buy")
run("trade_sell")
```
and execute the following command:
```
python main.py
```