# logger.py

from loguru import logger
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    os.path.join(LOG_DIR, "queries.log"),
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

def log_query_response(query: str, response: str):
    """
    Append a single line with the query and response.
    """
    logger.info(f"QUERY: {query} | RESPONSE: {response}")
