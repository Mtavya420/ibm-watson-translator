import unittest
from translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.Testcase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None), None)
    def test_englishToFrench(self):    
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    class TestfrenchToEnglish(unittest.Testcase):
     def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


    if __name__ == '__main__':
        unittest.main()