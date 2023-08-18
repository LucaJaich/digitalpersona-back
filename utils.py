import cv2
import numpy as np
from typing import List

class Serializer:
    def __encode_keypoint(self, keypoint):
        return (keypoint.pt)

    def encode(self, keypoints: List[cv2.KeyPoint], desc, path):
        temps = []
        for keypoint in keypoints:
            temps.append(self.__encode_keypoint(keypoint))

        serialized = (temps, desc)
        try:
            with open("test.h5", 'wb') as output_file:
                np.savez(
                    output_file,
                    keypoints=serialized,
                )
                return True
        except Exception as e:
            print("Error saving :",e)
            return False
        
        

if __name__ == "__main__":
    print("aa")
    kp: cv2.KeyPoint = cv2.KeyPoint(2, 3, 4)
    print(kp)
    # ser = Serializer()
    # ser.encode_keypoint()
