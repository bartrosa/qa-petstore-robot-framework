import os
from dotenv import load_dotenv


class SetEnvironment:
    def __init__(self):
        load_dotenv()

    def get_env_variable(self, key, default=None):
        return os.getenv(key, default)

env = SetEnvironment()
