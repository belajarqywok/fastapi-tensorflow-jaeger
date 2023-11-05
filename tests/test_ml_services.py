import unittest
from src.services.ml_services.nlp_service import nlp_service

class ml_service_tests(unittest.TestCase):
    # NLP Service Test
    def test_nlp_service(self) -> None:
        # Question
        question: str = "mental"

        # NLP Service
        service = nlp_service()

        # Answer
        answer: str = service.predict_question(question)

        self.assertTrue(question in answer.lower())