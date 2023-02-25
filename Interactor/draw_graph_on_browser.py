import json
import os
import subprocess
import sys

from Entities import EntitiesABC
from Gateway import GatewayABC


def execute(e: EntitiesABC, g: GatewayABC, save, feedback, **kwargs):
    save()
    path = g.script_json_path
    data = g.load_json(path)
    color_options = g.load_json(g.color_options_json_path)
    if color_options is not None:
        kwargs.update({'color_options': color_options})
    python_path, script_path = read_python_path_and_script_path(data, path, feedback)

    if None not in [python_path, script_path]:
        pickle_path = g.auto_save_path
        card_id = e.active_card.id
        graph_path = g.graph_folder_path
        draw_graph_on_browser(card_id, graph_path, pickle_path, python_path, script_path, **kwargs)
    feedback_graphing_error(feedback, path, python_path, script_path)


def read_python_path_and_script_path(data, path, feedback):
    if data is None:
        message = f"Could not read Script path file.\nCheck {path}."
        feedback("Invalid script path file", message)
    python_path = None
    script_path = None
    if data is not None:
        python_path = data.get('python_path', None)
        script_path = data.get('graph_script_path', None)

    return python_path, script_path


def feedback_graphing_error(feedback, path, python_path, script_path):
    if python_path is None:
        message = f"Python path {python_path} is invalid.\nCheck {path}."
        feedback("Invalid python path", message)
    elif script_path is None:
        message = f"Scrip path {script_path} is invalid.\nCheck {path}."
        feedback("Invalid script path", message)


def draw_graph_on_browser(card_id, graph_path, pickle_path, python_path, script_path, **kwargs):
    if sys.platform == 'darwin':
        argv = [
            f'"{pickle_path}"',
            f'"{card_id}"',
            f'"{graph_path}"',
            str(kwargs.get('configure_dynamically', False)),
            json.dumps(kwargs.get('color_options', {})),
        ]
        command = f'''
        "{python_path}" "{script_path}" {argv[0]} {argv[1]} {argv[2]} {argv[3]} '{argv[4]}'
        '''
        os.system(command)
    else:
        argv = [
            pickle_path,
            card_id,
            graph_path,
            str(kwargs.get('configure_dynamically', False)),
            json.dumps(kwargs.get('color_options', {})),
        ]
        command = '"' + '" "'.join([python_path, script_path] + argv) + '"'
        subprocess.call(command)
