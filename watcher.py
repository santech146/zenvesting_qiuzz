import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TranscriptHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("transcript.txt"):
            print(f"Detected change in {event.src_path}. Regenerating quiz...")
            try:
                subprocess.run(["python", "generator.py"], check=True)
                print("Quiz regenerated successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error regenerating quiz: {e}")

if __name__ == "__main__":
    path = "data"
    event_handler = TranscriptHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    
    print(f"Watching {path} for transcript changes...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
