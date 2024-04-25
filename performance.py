import json
import subprocess
import threading
import time

import psutil
import psycopg2
import requests

from db.postgres import PGDatabase


def monitor_resources():
    process = psutil.Process()  # Get current process
    while process.is_running():
        cpu_usage = process.cpu_percent(interval=0.1)
        memory_usage = process.memory_info().rss  # in bytes
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage / (1024 * 1024)} MB")


# Database connection parameters


def bla(db: PGDatabase):
    # Connect to your PostgreSQL database
    monitor_resources()
    db.execute("select * from graph_view LIMIT 1")
    db.cur.fetchall()
    # cursor.execute("SELECT NOW();")  # Simple query to fetch current time
    # print("Database time:", cursor.fetchone())

    # Monitor resources while connected


def spawn_process(command):
    # Start the process
    process = subprocess.Popen(command, shell=True)
    return process


def monitor_process(pid):
    try:
        process = psutil.Process(pid)
        # Continuously monitor the process
        while True:
            if process.is_running():
                cpu_usage = process.cpu_percent(interval=0.1)
                memory_usage = process.memory_info().rss  # in bytes
                print(f"CPU Usage: {cpu_usage}%")
                print(f"Memory Usage: {memory_usage / (1024 * 1024)} MB")
            else:
                print("Process has terminated.")
                break
    except psutil.NoSuchProcess:
        print("No process found.")


if __name__ == "__main__":
    db = PGDatabase(8000)
    db.start()

    bla(db)

    # db.execute("select * from graph_view LIMIT 1")
    # Specify the command you want to run as a process
    # command = "psql -1 -h 127.0.0.1 -p 8000 --user=postgres -c 'select * from graph_view LIMIT 1;'"
    # proc = spawn_process(command)
    # print(f"Monitoring process with PID: {proc.pid}")
    # monitor_process(proc.pid)
