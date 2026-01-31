import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
print(LOG_LEVEL)

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger("demo")

def main():
    logger.debug("debug: starting up")
    logger.info("info: app started")
    for i in range(5):
        logger.info("info: tick %d", i)
        if i == 2:
            logger.warning("warn: simulated slow path at i=%d", i)
        time.sleep(1)
    logger.error("error: simulated failure marker (not raising)")

if __name__ == "__main__":
    main()