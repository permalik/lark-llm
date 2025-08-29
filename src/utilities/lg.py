import os

from loguru import logger

log_dir = "/Users/tymalik/Docs/Git/lark/lark-llm/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "out.log")
logger.remove()
logger.add(
    log_file,
    format="{time} | {level} | {message}",
    level="DEBUG",
    serialize=True,
    rotation="10 MB",
    retention="7 days",
)
