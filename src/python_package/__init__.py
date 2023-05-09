__version__ = '0.0.1'

import shlex
import subprocess
import traceback
from typing import Any

from flask import Flask, jsonify, request, Response


def exception(e: Exception) -> Response:
    return jsonify(
        error=True,
        exception=type(e).__name__,
        traceback=traceback.format_exc()
    )


def shell_output(cp: subprocess.CompletedProcess) -> Response:
    return jsonify(
        error=False,
        returncode=cp.returncode,
        stdout=cp.stdout.decode('utf-8'),
        stderr=cp.stderr.decode('utf-8')
    )


def python_output(o: Any) -> Response:
    return jsonify(
        error=False,
        output=o
    )


def error(message: str) -> Response:
    return jsonify(
        error=True,
        message=message
    )


def get_command() -> Response | str:
    if request.is_json:
        try:
            command = request.get_json()['command']
        except (KeyError, ValueError) as e:
            return exception(e)
    elif request.method == 'POST':
        command = request.form.get('command')
    else:
        command = request.args.get('command')

    if not command:
        return error('Command is empty')

    if type(command) is not str:
        return error('Command must be string')

    return command


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/shell', methods=['GET', 'POST'])
    def shell():
        command = get_command()

        if type(command) is Response:
            return command

        try:
            cp = subprocess.run(shlex.split(command), capture_output=True)
            return shell_output(cp)

        except Exception as e:
            return exception(e)

    @app.route('/info', methods=['GET'])
    def info():
        return jsonify(
            version=__version__,
        )

    return app
