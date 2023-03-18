# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
from PIL import Image
import base64

from io import BytesIO


img = Image.open("../mtailor_mlops_assessment/n01667114_mud_turtle.JPEG")
im_file = BytesIO()
img.save(im_file, format="JPEG")
im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
im_b64 = base64.b64encode(im_bytes)

model_inputs = {'input': im_b64.decode()}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())