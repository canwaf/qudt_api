import requests
import hashlib
import datetime
from pathlib import Path, PurePath
import logging

logger = logging.getLogger(__name__)

class HttpCachedFile:
    def __init__(self, url=str, cache_dir=Path('./.cache')):
        self.url = url
        self.cache_dir = Path(cache_dir)
        self.filename = hashlib.md5(url.encode('utf-8')).hexdigest()
        self.filepath = self.cache_dir / self.filename

        if not self.cache_dir.exists():
            self.cache_dir.mkdir(parents=True)

        if (not self.filepath.exists()) or (datetime.datetime.now() - datetime.datetime.fromtimestamp(self.filepath.stat().st_mtime) > datetime.timedelta(days=1)):
            logger.info(f"Downloading file from {url}")
            response = requests.get(url)
            with open(self.filepath, 'wb') as f:
                f.write(response.content)
            logger.info(f"File downloaded and saved to {self.filepath}")
        else:
            logger.info(f"File already exists in cache: {self.filepath}")
