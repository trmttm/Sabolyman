import os

from sabolyman import main


def start_app():
    main.start_app(os.path.join('sabolyman', 'gui01.gui'))


start_app()
