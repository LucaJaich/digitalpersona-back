from flask import Flask, request
from flask_cors import CORS
import cv2
import base64
import numpy as np
from utils import Serializer

app = Flask(__name__)
cors = CORS(app, resources={r"/register": {"origins": "*"}})

@app.route('/register', methods=['POST'])
def register():
    #recieve image
    print(request.json.get('data')[:50])
    im_bytes = base64.b64decode(request.json.get('data') + '==')
    decoded = cv2.imdecode(np.frombuffer(im_bytes, np.uint8), -1)

    sift = (cv2.SIFT_create())

    keypoints_1, des1 = sift.detectAndCompute(decoded, None)
    print(keypoints_1, type(keypoints_1))

    s = Serializer()
    s.encode(keypoints_1, des1, "test.h5")

    # with open("test.h5", 'wb') as output_file:
    #     np.savez(
    #         output_file,
    #         keypoints=keypoints_1,
    #         descriptors=des1
    #     )


    keypoints_2, des2 = sift.detectAndCompute(decoded, None)

    # matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, {}).knnMatch(
    #     des1, des2, k=2
    # )

    print('saved correctly')
    return 'success'

if __name__ == '__main__':
    app.run()
