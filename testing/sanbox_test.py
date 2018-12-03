import unittest


class TestSandbox(unittest.TestCase):
    pass


def main():
    unittest.TestLoader().loadTestsFromTestCase(TestSandbox).run()


if __name__ == "__main__":
    main()