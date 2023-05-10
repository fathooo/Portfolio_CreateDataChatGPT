from app.config import environments
from app.config.logger import logger


@logger()
def run_app():
    app = "RUNNING APP"
    return app

