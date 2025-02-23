import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    INCORRECT_LOGIN = os.getenv("INCORRECT_LOGIN")
    INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")