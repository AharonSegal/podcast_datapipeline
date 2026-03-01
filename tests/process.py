#audio & metadata

from pathlib import Path
import os
import datetime

# Create a Path object for the file you want to inspect
audio_path = Path('download (1).wav')

def audio_file_process(path):
    """
    gets: file path
    returns: audio to text and metadata
    """
audio_path = Path(path)

# Get the file statistics
metadata = audio_path.stat()

if audio_path.exists():
    stats = audio_path.stat()
    print(f"File: {audio_path.name}")
    print(f"Size: {stats.st_size} bytes")
    # Convert modification time to readable format
    mtime = datetime.datetime.fromtimestamp(stats.st_mtime)
    print(f"Last Modified: {mtime}")


# Create a Path object for the file you want to inspect
audio_path = Path('download (1).wav')

# Get the file statistics
metadata = audio_path.stat()

if audio_path.exists():
    stats = audio_path.stat()
    print(f"File: {audio_path.name}")
    print(f"Size: {stats.st_size} bytes")
    # Convert modification time to readable format
    mtime = datetime.datetime.fromtimestamp(stats.st_mtime)
    print(f"Last Modified: {mtime}")