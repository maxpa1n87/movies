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
    full_path = None
    file_size = 0
    new_path = None

    if field_name in request.files:
        file = request.files[field_name]

    if file and file.filename != '':
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0, os.SEEK_SET)
        if file_size > current_app.config['MAX_UPLOAD_SIZE']:
            raise RequestEntityTooLarge()
        
        filename = secure_filename(file.filename)
        suffix= pathlib.Path(filename).suffix
        only_filename = token_hex() + suffix
        if os.path.isabs(current_app.config['UPLOAD_FOLDER']):
            new_path = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            full_path = os.path.join(new_path, only_filename)
        else:
            new_path = os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'])
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            full_path = os.path.join(new_path, only_filename)
        file.save(full_path, current_app.config['MAX_BUFFER_SIZE_FOR_FILE'])
        new_image = Image.open(full_path)
        fixed_image = ImageOps.exif_transpose(new_image)
        fixed_image.thumbnail((current_app.config['THUMBNAIL_IMAGE_WIDTH'], current_app.config['THUMBNAIL_IMAGE_HEIGHT']))
        fixed_image.save(full_path)
        new_image.close()
        fixed_image.close()
        return only_filename
    
    return None

def delete_old_file(filename):
    full_path = None

    if filename is not None:
        if os.path.isabs(current_app.config['UPLOAD_FOLDER']):
            full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        else:
            full_path = os.path.join(os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER']), filename)
        if os.path.exists(full_path):
            os.remove(full_path)
