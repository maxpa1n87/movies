from flask import Blueprint, current_app, send_from_directory
import os

bp = Blueprint('download', __name__)

@bp.route('/uploads/<name>')
def download_file(name):
    full_path = None

    if os.path.isabs(current_app.config['UPLOAD_FOLDER']):
        full_path = current_app.config['UPLOAD_FOLDER']
    else:
        full_path = os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'])

    return send_from_directory(full_path, name)
