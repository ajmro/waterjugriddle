import unittest
import json
from waterjug import waterjugrequest

class TestSum(unittest.TestCase):

    def test_steps(self):
        result = json.loads(waterjugrequest(2, 10, 4))
        self.assertEqual(result['Best Solution'], '4 steps')
        
        result = json.loads(waterjugrequest(5, 3, 4))
        self.assertEqual(result['Best Solution'], '6 steps')
        
        result = json.loads(waterjugrequest(2, 100, 96))
        self.assertEqual(result['Best Solution'], '4 steps')
        
    def test_values(self):
        result = json.loads(waterjugrequest(2, 0, 4))
        self.assertEqual(result['Error'], 'One of the variables is not greater than 0')
        
        result = json.loads(waterjugrequest(2, 3, 'x'))
        self.assertEqual(result['Error'], 'One of the variables is not an integer')
        
        result = json.loads(waterjugrequest(2, 3.3, 6))
        self.assertEqual(result['Error'], 'One of the variables is not an integer')
        
        result = json.loads(waterjugrequest(2, 4, 5))
        self.assertEqual(result['Error'], 'Z is greater than X and Y')
        
    def test_no_solution(self):
        result = json.loads(waterjugrequest(2, 6, 5))
        self.assertEqual(result['Error'], 'No Solution')
        
if __name__ == '__main__':
    unittest.main()

