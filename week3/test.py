import unittest
import ast
from mock import Mock, patch
from doc import get_docstring


class Test(unittest.TestCase):

    @patch("ast.get_docstring")
    def test_get_docstring(self, mock_get_docstring):
        mock_get_docstring.return_value = "Test docstring"
        result = get_docstring(ast.FunctionDef)
        self.assertEqual(result, "Test docstring")
        
    
        
if __name__ == '__main__':
    unittest.main()