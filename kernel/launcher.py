# modify from https://github.com/microsoft/TaskWeaver/blob/main/taskweaver/ces/kernel/launcher.py
import os
import sys

from kernel.ext import TaskWeaverZMQShellDisplayHook
from kernel.kernel_logging import logger


def start_app():
    from ipykernel.kernelapp import IPKernelApp

    from ipykernel.zmqshell import ZMQInteractiveShell

    # override displayhook_class for skipping output suppress token issue
    ZMQInteractiveShell.displayhook_class = TaskWeaverZMQShellDisplayHook

    app = IPKernelApp.instance()
    app.name = "code_executor"
    app.config_file_name = os.path.join(os.path.dirname(__file__), "config.py")
    app.extensions = []
    app.language = "python"

    session_id = os.getenv("SESSION_ID", "session_id")
    kernel_id = os.getenv("KERNEL_ID", "kernel_id")
    connection_file = os.getenv(
        "CONNECTION_FILE", f"/app/conn/conn-{session_id}-{kernel_id}.json"
    )

    ip = os.getenv("KERNEL_IP", "0.0.0.0")
    port_start = int(os.getenv("KERNEL_PORT_START", "5555"))

    app.connection_file = connection_file
    app.shell_port = port_start
    app.iopub_port = port_start + 1
    app.stdin_port = port_start + 2
    app.hb_port = port_start + 3
    app.control_port = port_start + 4
    app.ip = ip

    cwd = os.getenv("KERNEL_CWD", "/app/cwd/")  # os.path.dirname(__file__))
    os.chdir(cwd)

    logger.info("Initializing app...")
    app.initialize()
    logger.info("Starting app...")
    app.start()


if __name__ == "__main__":
    if sys.path[0] == "":
        del sys.path[0]
    logger.info("Starting process...")
    logger.info("sys.path: %s", sys.path)
    logger.info("os.getcwd(): %s", os.getcwd())
    start_app()
