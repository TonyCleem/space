from pathlib import Path


def creates_directory_for_image_path():
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    return path
