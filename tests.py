import os
import bitly
import unittest
import tempfile

class BitlyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        bitly.app.config['TESTING'] = True
        self.app = bitly.app.test_client()
        bitly.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bitly.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
