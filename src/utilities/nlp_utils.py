import re
from typing import Any
from pickle import load
from keras import models 

# NLP Utilities
class nlp_utils:
    def __init__(self) -> None :
        # Load HDF5 Model
        self.__model = models.load_model(
            filepath = './ml_models/capstone_model.h5'
        )

        # Tokenizer
        self.__tokenizer: Any = load(
            file = open('./ml_models/tokenizer.pickle', 'rb')
        )

        # Label Encoder
        self.__label_encoder: Any = load(
            file = open('./ml_models/label_encoder.pickle', 'rb')
        )


    # Clean Stopwords
    def clean_stopwords(self, sentence: str) -> str:
        stopwords = []
        with open('./ml_models/stopwords.txt', encoding='utf-8') as read_stopwords:
            for line_stopword in read_stopwords:
                stopwords.append(line_stopword.strip())

        temp = [word for word in sentence.split() if word not in stopwords]
        temp = " ".join(temp)
        temp = re.sub(r'[.,’"\'-?:!;]', '', temp)
        temp = re.sub(r'^whats|^im', '', temp)

        return temp.strip()

    # Model
    @property
    def model(self) -> Any:
        return self.__model

    # Tokenizer
    @property
    def tokenizer(self) -> Any:
        return self.__tokenizer

    # Label Encoder
    @property
    def label_encoder(self) -> Any:
        return self.__label_encoder
