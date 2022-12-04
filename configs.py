# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "6216349"))
    API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5880563885:AAHf0Fi8x_iNDfHmpL0y03KO3sUxnn_ZlE0")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1823080600))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1823080600").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://asubang:asubang@cluster0.gbyc7wo.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
