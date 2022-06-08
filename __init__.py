import os

from sabolyman import main


def start_app():
    main.start_app(os.path.join('GUI', 'gui01.gui'))


start_app()
