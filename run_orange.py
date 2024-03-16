import os
import signal
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Command to start Orange Canvas
orange_command = ["orange-canvas"]

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Restart Orange Canvas when any file is modified
        restart_orange_canvas()

def restart_orange_canvas():
    global orange_process

    if orange_process is not None:
        # Terminate the existing Orange Canvas process
        os.kill(orange_process.pid, signal.SIGTERM)
        orange_process.wait()

    # Start Orange Canvas
    orange_process = subprocess.Popen(orange_command)

def main():
    global orange_process

    orange_process = None

    # Start Orange Canvas
    restart_orange_canvas()

    # Start a watchdog observer
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopping...")
        sys.exit()

if __name__ == "__main__":
    main()