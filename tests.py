import unittest

import hello as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        self.assertEqual(
            r.data.decode('utf-8'), 
            'I did it! You can read more about this app -> ' + 
            'https://github.com/MariaMozgunova/flask-app'
        )

    def test_post(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()
