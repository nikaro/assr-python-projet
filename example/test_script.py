#!/usr/bin/python3

import unittest

import script


class TestSuite(unittest.TestCase):
    def test_main_count_zero(self):
        url = "toto"
        passwd = "tata"
        self.assertEqual(script.check_if_pwned_example(url, passwd), 0)


if __name__ == "__main__":
    unittest.main()
