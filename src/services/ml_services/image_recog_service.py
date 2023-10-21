import os
import shutil
from fastapi import UploadFile
from src.utilities.image_recog_utils import image_recog_utils

class image_recog_service:
    # Image Recog Utils
    __IMAGE_RECOG_UTILS = image_recog_utils()

    def predict_image(self, file: UploadFile) -> str:
        upload_dir = os.path.join(os.getcwd(), "uploads")

        # Create the upload directory if it doesn't exist
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # get the destination path
        dest = os.path.join(upload_dir, file.filename)

        # copy the file contents
        with open(dest, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        object_name = self.__IMAGE_RECOG_UTILS.get_object_name(
            filename = file.filename
        )

        os.remove(f"./uploads/{file.filename}")

        return object_name
