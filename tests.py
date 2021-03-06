import os
import bitly
import unittest
import tempfile

class BitlyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, bitly.app.config['DATABASE'] = tempfile.mkstemp()
        bitly.app.config['TESTING'] = True
        self.app = bitly.app.test_client()
        bitly.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bitly.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No urls entered' in rv.data

    def test_url_entry(self):
        rv = self.app.post('/add', data=dict(
            title='<www.google.com'), follow_redirects=True)
        assert 'No urls entered' not in rv.data
        assert 'www.google.com' in rv.data
if __name__ == '__main__':
    unittest.main()
