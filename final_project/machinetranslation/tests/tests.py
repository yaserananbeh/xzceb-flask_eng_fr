import unittest


from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    '''docstring'''

    def test_e2f(self):
        '''docstring'''

        self.assertEqual(english_to_french("Hello"),
                         "Bonjour", 'Wrong translation')
        self.assertNotEqual(english_to_french("Hello"),
                            "Hello", 'Wrong translation')

    def test_f2e(self):
        '''docstring'''

        self.assertEqual(french_to_english("Bonjour"),
                         "Hello", 'Wrong translation')
        self.assertNotEqual(french_to_english("Bonjour"),
                            "Bonjour", 'Wrong translation')


if __name__ == '__main__':
    unittest.main()
