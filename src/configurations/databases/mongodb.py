import os
from dotenv import load_dotenv
from motor import motor_asyncio

load_dotenv()


# MongoDB Configuration
class mongo_config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self) -> None:
        self.client = motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_URL'))
        self.db = self.client[os.getenv('MONGO_DBNAME')]

    def close_connection(self) -> None:
        self.client.close()
    