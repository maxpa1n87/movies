from flask import Blueprint, current_app, send_from_directory

bp = Blueprint('download', __name__)

@bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)
