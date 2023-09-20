from keras import utils
from typing import Type, Any
from numpy import ndarray, argmax
from src.utilities.ml_utils import ml_utils

# Prediction Service
class prediction_service:
    # Machine Learning Utils
    __ML_UTILS = ml_utils()

    # Predict Question
    def predict_question(self, question: str) -> str:
        # Clean Question
        clean_question: str = self.__ML_UTILS.clean_stopwords(
            sentence = question
        )

        # Sequences
        sequences: Type[ndarray] = utils.pad_sequences(
            sequences = self.__ML_UTILS.tokenizer.texts_to_sequences([clean_question])
        )

        # Predict
        predict: Any = self.__ML_UTILS.model.predict(sequences)

        # Inverse Transform Label Encoder
        return self.__ML_UTILS.label_encoder.inverse_transform(
            [argmax(predict)]
        )[0]