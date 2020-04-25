# -*- coding: utf-8 -*-
import logging
import logging.config
import socket

import yaml

from FlaskPyqtOrganizer import FlaskPyqtOrganizer
from app import app

target_host = 'localhost'
min_port = 49152
max_port = 65535

logging.config.dictConfig(yaml.load(open('logging.yaml'), Loader=yaml.FullLoader))
logger = logging.getLogger(__name__)


def get_free_port():
    for port in range(min_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return_code = s.connect_ex((target_host, port))

        if return_code != 0:
            logger.info("Port %d can use!" % (port))
            return port


if __name__ == '__main__':
    FlaskPyqtOrganizer(app, host=target_host, port=get_free_port()).run()
