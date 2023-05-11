
from app.config.logger import logger

from app.functions.chainOfThought import THOUGHT_1
from app.functions.openAI import getResponseAI

@logger()
def run_app():
    print(getResponseAI(THOUGHT_1))
    # input("Press Enter to close...")
    app = "RUNNING APP"
    return app

