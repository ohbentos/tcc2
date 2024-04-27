import os
import signal
import sys

PID = 0


def signal_handler(signal, frame):
    global PID

    print("Signal received, terminating...")
    os.kill(PID, 9)
    sys.exit(0)


def setup_signals():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


setup_signals()
