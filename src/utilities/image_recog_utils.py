import numpy as np
from keras.models import load_model
from keras.utils import load_img, img_to_array

# Image Recog Utilities
class image_recog_utils:
    # Model
    __MODEL = load_model('./ml_models/model.h5')

    def __init__(self) -> None:
        self.__labels: list = ['kertas', 'batu', 'gunting']

    def get_object_name(self, filename: str) -> str:
        # Load Image
        load_image = load_img(
            path = f"./uploads/{filename}", 
            target_size = (150, 150)
        )

        # Expand Dimension
        expand_dimension = np.expand_dims(
            axis = 0,
            a = img_to_array(img = load_image)
        )

        # Stack arrays in sequence vertically
        vert_stack_image = np.vstack(
            tup = [expand_dimension]
        )

        # Predict
        predict = self.__MODEL.predict(
            batch_size = 16,
            x = vert_stack_image
        )

        message = 'gambar tidak diketahui'
        for idx_predict in range(len(self.__labels)) :
            if predict[0][idx_predict] == 1 :
                message = f"Ini adalah gambar {self.__labels[idx_predict]}"
                break

        return message
