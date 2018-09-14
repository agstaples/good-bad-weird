import unittest
import markov


class TestCase(unittest.TestCase):

    def test_make_word_tuples(self):
        self.assertEqual(len(markov.make_word_tuples()), 5039)
        self.assertEqual(len(markov.make_word_tuples(1)), 2294)
        self.assertEqual(len(markov.make_word_tuples(2)), 5039)
        self.assertEqual(len(markov.make_word_tuples(3)), 6108)
        self.assertEqual(markov.make_word_tuples(), markov.make_word_tuples(2))


    def test_random_forward_markov(self):
        self.assertIsNotNone(markov.random_forward_markov())
        self.assertNotIn("||", markov.random_forward_markov())


    def test_multi_directional_markov(self):
        self.assertIsNotNone(markov.multi_directional_markov("the"))
        self.assertIsNotNone(markov.multi_directional_markov("the", 1))
        self.assertIsNotNone(markov.multi_directional_markov("the", 2))
        self.assertIsNotNone(markov.multi_directional_markov("the", 3))
        self.assertIn("the", markov.multi_directional_markov("the")[0])
        self.assertIn("the", markov.multi_directional_markov("the", 1)[0])
        self.assertIn("the", markov.multi_directional_markov("the", 2)[0])
        self.assertIn("the", markov.multi_directional_markov("the", 3)[0])
        self.assertNotIn("||", markov.multi_directional_markov("the")[0])
        self.assertNotIn("||", markov.multi_directional_markov("the", 1)[0])
        self.assertNotIn("||", markov.multi_directional_markov("the", 2)[0])
        self.assertNotIn("||", markov.multi_directional_markov("the", 3)[0])
        self.assertTrue(int(markov.multi_directional_markov("the")[1]))
        self.assertTrue(int(markov.multi_directional_markov("the", 1)[1]))
        self.assertTrue(int(markov.multi_directional_markov("the", 2)[1]))
        self.assertTrue(int(markov.multi_directional_markov("the", 3)[1]))


if __name__ == "__main__":
    unittest.main()