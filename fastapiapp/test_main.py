# from fastapi.testclient import TestClient
# from main import app
#
# client = TestClient(app)

from config import get_settings
import os

from fastapiapp.sql_app.schema import User
from logger.loguruTest import logger




if __name__ == "__main__":
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(current_file_path)
    applog_folder = os.path.join(project_root, "applog")
    logger.info(os.path.dirname)
    logger.info(current_file_path)
    logger.info(project_root)
    # print(os.path.basename())
    logger.info(applog_folder)
    # print(get_settings())
    # logger.info("from test_main")
    # user_base = User(id=1, email='12342', items=[], is_active=False)
    # logger.error("创建用户异常{}", user_base)
