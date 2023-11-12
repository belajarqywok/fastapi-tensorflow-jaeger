from keras import utils
from typing import Type, Any
from numpy import ndarray, argmax
from src.utilities.nlp_utils import nlp_utils

# NLP Service
class nlp_service:
    # NLP Utils
    __NLP_UTILS = nlp_utils()

    # Predict Question
    def predict_question(self, question: str) -> str:
        # Clean Question
        clean_question: str = self.__NLP_UTILS.clean_stopwords(
            sentence = question
        )

        # Sequences
        sequences: Type[ndarray] = utils.pad_sequences(
            sequences = self.__NLP_UTILS.tokenizer.texts_to_sequences([clean_question])
        )

        # Predict
        predict: Any = self.__NLP_UTILS.model.predict(sequences)

        # Inverse Transform Label Encoder
        return self.__NLP_UTILS.label_encoder.inverse_transform(
            [argmax(predict)]
        )[0]
        