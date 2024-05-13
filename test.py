import unittest
import json
from waterjug import waterjugrequest

class TestSum(unittest.TestCase):

    def test_steps(self): # This test evaluates an outcome knowing the number of steps for the best solution
        result = json.loads(waterjugrequest(2, 10, 4))
        self.assertEqual(result['Best Solution'], '4 steps')
        
        result = json.loads(waterjugrequest(5, 3, 4))
        self.assertEqual(result['Best Solution'], '6 steps')
        
        result = json.loads(waterjugrequest(2, 100, 96))
        self.assertEqual(result['Best Solution'], '4 steps')
        
        # result = json.loads(waterjugrequest(X, Y, Z))  Replace X, Y, Z with desired values
        # self.assertEqual(result['Best Solution'], 'N steps')   Replace N with number of steps 
        
    def test_values(self): # This test evaluates the limitations and data validation. Available error strings are: ['One of the variables is not greater than 0', 'Z is greater than X and Y', 'One of the variables is not an integer', 'No Solution']
        result = json.loads(waterjugrequest(2, 0, 4)) 
        self.assertEqual(result['Error'], 'One of the variables is not greater than 0')
        
        result = json.loads(waterjugrequest(2, 3, 'x'))
        self.assertEqual(result['Error'], 'One of the variables is not an integer')
        
        result = json.loads(waterjugrequest(2, 3.3, 6))
        self.assertEqual(result['Error'], 'One of the variables is not an integer')
        
        result = json.loads(waterjugrequest(2, 4, 5))
        self.assertEqual(result['Error'], 'Z is greater than X and Y')
        
        result = json.loads(waterjugrequest(2, 6, 5))
        self.assertEqual(result['Error'], 'No Solution')
        
        # result = json.loads(waterjugrequest(X, Y, Z))  Replace X, Y, Z with desired values
        # self.assertEqual(result['Error'], 'String')   Replace String with expected error string
        
        
if __name__ == '__main__':
    unittest.main()

