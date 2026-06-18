from flask import current_app
from werkzeug.utils import secure_filename
import pathlib
import os
from secrets import token_hex
from PIL import Image, ImageOps
from werkzeug.exceptions import RequestEntityTooLarge

def upload_file(request, field_name):
    file = None
    filename = None   
    root_path = None

    if field_name in request.files:
        file = request.files[field_name]

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        suffix= pathlib.Path(filename).suffix
        only_filename = token_hex(8) + suffix
        if os.path.isabs(current_app.config['UPLOAD_FOLDER']):
            root_path = os.path.join(current_app.config['UPLOAD_FOLDER'], only_filename)
        else:
            root_path = os.path.join(os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER']), only_filename)
        file.save(root_path, current_app.config['MAX_BUFFER_SIZE_FOR_FILE'])
        new_image = Image.open(root_path)
        fixed_image = ImageOps.exif_transpose(new_image)
        fixed_image.thumbnail((255, 255))
        fixed_image.save(root_path)

        return os.path.join('uploads', only_filename)
    
    return None

def delete_old_file(filename):
    root_path = None

    if filename is not None:
        if os.path.isabs(current_app.config['UPLOAD_FOLDER']):
            root_path = os.path.join(current_app.config['UPLOAD_FOLDER'], str(filename).split(os.sep)[1])
        else:
            root_path = os.path.join(os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER']), str(filename).split(os.sep)[1])
        if os.path.exists(root_path):
            os.remove(root_path)
