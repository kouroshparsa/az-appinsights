"""
Validates the package
copyright: (c) 2023 by Kourosh Parsa.
"""
import unittest
from unittest.mock import patch
import az_sights


class TestInsights(unittest.TestCase):
    """ tests app insights result conversion """

    SAMPLE_OUTPUT = '{"tables": [{"columns": [{"name": "id"}, {"name": "label"}], "rows": ["a", "b"]}]}'
    @patch('az_sights.check_extensions')
    @patch('az_sights.execute', return_value=(SAMPLE_OUTPUT, '', 0))
    def test_query_today(self):
        """ tests query_today """
        res = az_sights.query_today('app_id', 'some query')
        self.assertEqual(res, [{'id': 'a'}, {'id': 'b'}])


if __name__ == '__main__':
    unittest.main()
