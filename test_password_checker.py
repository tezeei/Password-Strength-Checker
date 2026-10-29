import unittest
from unittest.mock import patch

from password_checker import check_password


class TestPasswordChecker(unittest.TestCase):

    def test_common_password(self):
        result = check_password("password")
        self.assertEqual(result["strength"], "Very Weak")

    def test_short_password(self):
        result = check_password("abc")
        self.assertEqual(result["strength"], "Weak")

    def test_moderate_password(self):
        result = check_password("BlueSky47")
        self.assertEqual(result["strength"], "Moderate")

    def test_strong_password(self):
        result = check_password("BlueSky!47River")
        self.assertEqual(result["strength"], "Strong")

    def test_entropy_is_nonnegative(self):
        result = check_password("BlueSky!47River")
        self.assertGreaterEqual(result["entropy"], 0)

    def test_repeated_characters(self):
        result = check_password("aaaa")
        self.assertEqual(result["score"], 0)

    def test_empty_password(self):
        result = check_password("")
        self.assertEqual(result["strength"], "Weak")

    def test_feedback_is_provided(self):
        result = check_password("abc")
        self.assertTrue(len(result["feedback"]) > 0)


if __name__ == "__main__":
    unittest.main()