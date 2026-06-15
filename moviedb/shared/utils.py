from flask import current_app
from werkzeug.utils import secure_filename
import moviedb
import pathlib
import os
from secrets import token_hex
from PIL import Image

def upload_file(request, field_name):
    file = None
    filename = None
    save_filename = None
    root_path = None

    if field_name in request.files:
        file = request.files[field_name]

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        suffix= pathlib.Path(filename).suffix
        only_filename = token_hex(8) + suffix
        save_filename = os.path.join(current_app.config['UPLOAD_FOLDER'], only_filename)
        if current_app.config['DEBUG']:
            root_path = os.path.join(current_app.root_path, save_filename)
        else:
            root_path = save_filename
        file.save(root_path)
        new_image = Image.open(root_path)
        new_image.thumbnail((255, 255))
        new_image.save(root_path)
        
        new_path = os.path.normpath(save_filename)
        splitted = new_path.split(os.sep)

        link_name = None
        index = 0

        for i in range(len(splitted)):
            if splitted[i] == 'uploads':
                index = i
                break

        link_name = os.path.join(splitted[index], splitted[len(splitted) - 1])

        return link_name
    
    return None

def delete_old_file(filename):
    root_path = None

    if filename is not None:
        if current_app.config['DEBUG']:
            root_path = os.path.join(current_app.root_path, filename)
        else:
            splitted = str(filename).split(os.sep)
            root_path = os.path.join(current_app.config['UPLOAD_FOLDER'], splitted[len(splitted) - 1])
        if os.path.exists(root_path):
            os.remove(root_path)
