# -*- coding: utf-8 -*-
import logging
from threading import Thread

from WebUi import WebUI

logger = logging.getLogger(__name__)


class FlaskPyqtOrganizer(object):
    def __init__(self, flask_app, *flask_args, **flask_kwargs):
        self.flask_app = flask_app
        self.flask_url = 'http://{host}:{port}'.format(**flask_kwargs)
        self.flask_thread = Thread(target=self._run_flask, args=flask_args, kwargs=flask_kwargs)
        self.flask_thread.daemon = True

    def run(self):
        logger.info('start flask with %s', self.flask_url)
        self.flask_thread.start()
        logger.info('start web ui')
        self._run_web_ui()

    def _run_web_ui(self):
        WebUI(url=self.flask_url).run_gui()

    def _run_flask(self, *args, **kwargs):
        self.flask_app.run(*args, **kwargs)
