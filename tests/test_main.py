from fastapi.testclient import TestClient
import structlog
import unittest


from app.main import app

logger = structlog.get_logger()


class TestGenerateRandomArray(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_generate_random_array(self):
        logger.info("TestGenerateRandomArray: test_generate_random_array started")

        sentence = "Hello, world!"
        dim = 500
        payload = {"sentence": sentence, "dim": dim}
        response = self.client.post("/generate_random_array/", json=payload)
        data = response.json()

        assert response.status_code == 200
        assert data["sentence"] == sentence
        assert len(data["sent_vec"]) == dim

        for value in data["sent_vec"]:
            assert isinstance(value, float)

        logger.info("TestGenerateRandomArray: test_generate_random_array completed")

    def test_generate_random_array_invalid_dim(self):
        logger.info("TestGenerateRandomArray: test_generate_random_array_invalid_dim started")

        sentence = "Hello, world!"
        dim = -10  # Invalid dimension
        payload = {"sentence": sentence, "dim": dim}
        response = self.client.post("/generate_random_array/", json=payload)

        assert response.status_code == 400

        logger.info("TestGenerateRandomArray: test_generate_random_array_invalid_dim completed")
