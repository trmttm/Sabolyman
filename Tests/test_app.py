import unittest


class MyTestCase(unittest.TestCase):
    def test_add_card(self):
        from sabolyman.main import start_app
        start_app()


if __name__ == '__main__':
    unittest.main()
