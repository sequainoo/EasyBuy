#!/usr/bin/python3
"""definition of Image upload view for a product """

import os

from flask import render_template, request, flash, url_for, redirect
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError

from web_app.admin_views import admin_views
from models import storage, Image
from utilities.small_helpers import valid_image_name


@admin_views.route('/image-upload/<phone_id>',
                   methods=['GET','POST'],
                   strict_slashes=False)
def image_upload_view(phone_id=''):
    """Upload an image for a phone.

    Images will be server under the /product-images/filename.ext url
    by the webserver.
    webserver will translate /product-images/ to UPLOAD_DIR
    """

    # define upload dir
    UPLOAD_DIR = '/var/easybuy/phone_image_uploads/'
    # create the directory
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if not phone_id or not storage.get('Phone', phone_id):
        flash('phone is not valid')
        return redirect(url_for('admin_views.phone_create_view'))

    if request.method == 'GET':
        return render_template('admin/image_upload_form.html')

    #  check the file part is included in the request
    if 'file' not in request.files:
        flash('File part not present')
        return redirect(request.url)

    image_file = request.files['file']
    # check that file was sent, empty filename means file was not sent
    if image_file.filename == '':
        flash('No file selected')
        return redirect(request.url)

    # build filesystem secure filename from the image name
    filename = secure_filename(image_file.filename)
    # make sure image is a valid image type with the right extension
    if not valid_image_name(filename):
        flash('Invalid image type')
        return redirect(request.url)

    # save image file now to the upload dir
    image_file.save(UPLOAD_DIR + filename)
    # create an image entry and save it in the database
    image = Image(phone_id=phone_id,
                  alt_text=filename.rsplit('.')[0].lower(),
                  url='/product-images/' + filename)
    try:
        storage.add(image)
        storage.save()
    except IntegrityError:
        flash('image has already been uploaded')
        storage.rollback()
        return redirect(request.url)

    flash('succesful you can add more')
    return redirect(request.url)
