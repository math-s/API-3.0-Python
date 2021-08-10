import os
from dotenv import load_dotenv

load_dotenv(override=True)

MERCHANT_ID = os.getenv('merchant_id')
MERCHANT_KEY = os.getenv('merchant_key')
