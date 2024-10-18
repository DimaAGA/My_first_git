import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_UKR_NET = os.getenv('TOKEN_UKR_NET')
USER = os.getenv('user')
SMTP_SERVER = os.getenv('smtp_server')
