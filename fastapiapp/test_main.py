# from fastapi.testclient import TestClient
# from main import app
#
# client = TestClient(app)

from config import get_settings

if __name__ == "__main__":
    print(get_settings())
