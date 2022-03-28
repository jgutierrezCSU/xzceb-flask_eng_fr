
import unittest
from translator import  englishToFrench, frenchToEnglish

class Testf2e(unittest.TestCase):
    """class translates french to english , then checks it"""
    def test1(self):
        """check Null"""
        self.assertNotEqual(frenchToEnglish("Bonjour"),None )
        # check f-e
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello" )
class Teste2f(unittest.TestCase):
    """class translates english to french , then checks it"""
    def test2(self):
        """ check null"""
        self.assertNotEqual(englishToFrench("Hello"), None)
        self.assertEqual(englishToFrench("Hello"),"Bonjour") #check e-f

unittest.main()
