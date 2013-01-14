
import unittest
import uuid

class MyTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_random_uuid(self):
        # make a random UUID
        my_uuid = uuid.uuid4()
        print my_uuid
