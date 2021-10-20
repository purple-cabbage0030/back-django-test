
import os
import numpy as np
import matplotlib.image as mpimg
from PIL import Image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
# %matplotlib inline

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model

# checkpoint_dir = os.getcwd()+"/model/"
model = load_model(os.getcwd()+'/best_model_.h5')

def image_data(filename):
    targetx = 128
    targety = 128

    test_dir = os.getcwd()+"/photos/"+filename
    print(test_dir)

    # image_path = []
    # for i in os.listdir(test_dir):
    #     test_image_name = test_dir + i
    #     image_path.append(test_image_name)  

    # for image in image_path:
    img = Image.open(test_dir)
    img = img.convert("RGB")
    img = img.resize((targetx,targety))    
    data = np.asarray(img)



    X = np.array(data)
    X = X.astype("float") / 256
    X = X.reshape(-1, targetx, targety,3)

    categories = [f'F{i}' for i in range(1,20)]
    pred = model.predict(X)  
    result = [np.argmax(value) for value in pred]   # 예측 값중 가장 높은 클래스 반환
    print('New image prediction : ',categories[result[0]])
    print("accuracy : {}".format(max(pred[0][0],pred[0][1],pred[0][2],pred[0][3],pred[0][4],pred[0][5],pred[0][6],pred[0][7],
                                        pred[0][8],pred[0][9],pred[0][10],pred[0][11],pred[0][12],pred[0][13],pred[0][14],pred[0][15],
                                        pred[0][16],pred[0][17],pred[0][18])))

    return categories[result[0]]


if __name__ == "__main__":
    image_data('egg.jpg')