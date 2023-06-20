from sabolyman import main
import sys

root_path = None
if len(sys.argv) > 1:
    root_path = sys.argv[1]


def start_app():
    main.start_app('gui04.gui', root_path)


start_app()
