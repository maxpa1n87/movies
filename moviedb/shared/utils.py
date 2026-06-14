from flask import current_app
from werkzeug.utils import secure_filename
import moviedb
import pathlib
import os
from secrets import token_hex
from PIL import Image

def upload_file(request):
    file = None
    filename = None
    save_filename = None
    new_filename = None

    if 'image' in request.files:
        file = request.files['image']

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        suffix= pathlib.Path(filename).suffix
        module_path = os.path.dirname(os.path.abspath(moviedb.__file__))
        full_path = os.path.join(module_path, current_app.config['UPLOAD_FOLDER'])
        if os.path.exists(full_path) == False:
            os.mkdir(full_path)   
        only_filename = token_hex(8) + suffix
        save_filename = os.path.join(full_path, only_filename)
        file.save(save_filename)
        new_image = Image.open(save_filename)
        new_image.thumbnail((255, 255))
        new_image.save(save_filename)
        new_filename = os.path.join(current_app.config['UPLOAD_FOLDER'], only_filename)
        
        return new_filename
    
    return None
