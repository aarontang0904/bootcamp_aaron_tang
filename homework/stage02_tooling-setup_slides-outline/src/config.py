import os
from dotenv import load_dotenv
from typing import Optional

def load_env():
    load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

if __name__ == "__main__":
    load_env()
    print("API_KEY present:", get_key("API_KEY"))