from flask import Flask, request
app = Flask(__name__)

"""
@api post /upload
description: This endpoint is for uploading images
tags:
    - api
responses:
    "201":
        description: Successfully uploaded an image
    "405":
        description: That method was not recognised
"""
@app.route("/upload", methods=['POST'])
    if request.method == 'POST':
        # submit an image
    else:
        # unrecognised method

"""
@api get /images/<image_name>
description: Load an image stored on the server
tags:
    - api
responses:
    "200":
        description: Successfully fetched an image
"""
@app.route("/img/<image_name>", methods=['GET'])
def get_image(image_name):
    if request.method == 'GET':
        # fetch image

"""
@api delete /images/<image_name>
description: Delete an image from the server
tags:
    - api
parameters:
    - in: query
      name: id
      description: The ID of an image to delete
      schema:
        type: integer
responses:
    "204":
        description: Successfully deleted an image
"""
@app.route("/img/<image_name>", methods=['DELETE'])
def images(image_name):
    if request.method == 'DELETE':
        # delete image
