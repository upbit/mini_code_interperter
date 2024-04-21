import os
import logging

logging.basicConfig(
    filename=os.environ.get("LOGGING_FILE_PATH", "kernel_runtime.log"),
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)
