import unittest
import server


class DadJokeIntegrationTestCase(unittest.TestCase):
    """testing Flask server"""

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_show_home(self):
        result = self.client.get("/home")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<input type="button" id="home-main-joke-btn" value="Generate Random Dad Joke">', result.data)

    def test_set_num_words(self):
        result = self.client.post("/set_num_words.json", data={"num_words": "3"})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"3", result.data)

    def test_return_random(self):
        result = self.client.get("/get_random_joke.json")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b' ', result.data)

    def test_return_not_random(self):
        result = self.client.post("/get_not_random_joke.json", data={"user_input": "the",
                                                                "joke_class": "red joke-text joke-2"})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'"joke-text joke-3"', result.data)

    def test_return_not_random(self):
        result = self.client.post("/get_not_random_joke.json", data={"user_input": "the",
                                                                "joke_class": "joke-text joke-4"})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'"joke-text joke-4"', result.data)


if __name__ == "__main__":
    unittest.main()