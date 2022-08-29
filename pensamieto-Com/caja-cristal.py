from cgi import test
import unittest

def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_mayor(self):
        edad = 20
        
        resultado = es_mayor(edad)
        
        self.assertEqual(resultado, True)
        
    def test_menor(self):
        edad = 15
        
        resultado = es_mayor(edad)
        
        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()