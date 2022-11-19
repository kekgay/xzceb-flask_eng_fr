import unittest
from translator import englishtofrench
from translator import frenchtoenglish

class testEnglishToFrench(unittest.TestCase):
    def test_englishtofrench(self):
       self.assertNotEqual(englishtofrench("None"),'')
       self.assertNotEqual(englishtofrench(0),0)
       self.assertEqual(englishtofrench('Hello'),'Bonjour')
       self.assertEqual(englishtofrench('Goodbye'),'Au revoir')

class testFrenchToEnglish(unittest.TestCase):
    def test_frenchtoenglish(self):
       self.assertNotEqual(frenchtoenglish("None"),'')
       self.assertNotEqual(frenchtoenglish(0),0)
       self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
       self.assertEqual(frenchtoenglish('Au revoir'),'Goodbye')

unittest.main()