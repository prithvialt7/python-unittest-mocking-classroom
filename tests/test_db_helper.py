from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class DbHelper(TestCase):
    def setUp(self):
        self.dbh = DbHelper()

    def test_max_salary_is_greater_than_min_salary(self):
        db_helper = DbHelper()
        max_sal = db_helper.get_maximum_salary()
        min_sal = db_helper.get_minimum_salary()
        self.assertGreater(max_sal, min_sal)

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        db_helper = MockDbHelper()  # create a mock object of Calculator class. This will help to customize output of class methods

        '''
        mock the sum() method of Calculator class to return value '1'. Noth that since we have mocked/stubbed the
        sum method, it will not execute the actual logic whenever called and just return 1 irrespective of input.
        '''
        db_helper.get_maximum_salary.return_value = 1  
        db_helper.get_minimum_salary.return_value = 0

        max_sal = db_helper.get_maximum_salary()
        min_sal = db_helper.get_minimum_salary()
        
        self.assertGreater(max_sal, min_sal)