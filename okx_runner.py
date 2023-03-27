from okx_client import OkxClient
from dotenv import load_dotenv
import os


class OkxRunner:

    def __init__(self):
        load_dotenv()

        self.ENVIRONMENT = os.getenv("ENVIRONMENT")

        self.API_KEY = ""
        self.API_SECRET = ""
        self.API_PASSPHRASE = ""

        if self.ENVIRONMENT == "PRODUCTION":
            self.API_KEY = os.getenv("API_KEY")
            self.API_SECRET = os.getenv("API_SECRET")
            self.API_PASSPHRASE = os.getenv("API_PASSPHRASE")
        else:
            self.API_KEY = os.getenv("DEMO_API_KEY")
            self.API_SECRET = os.getenv("DEMO_API_SECRET")
            self.API_PASSPHRASE = os.getenv("DEMO_API_PASSPHRASE")

        self.is_demo_mode = self.ENVIRONMENT != "PRODUCTION"

        self.okx_client = OkxClient(
            self.API_KEY,
            self.API_SECRET,
            self.API_PASSPHRASE,
            self.is_demo_mode
        )
