"""Tests for greeting helpers."""

import unittest

from silver_journey import build_greeting


class BuildGreetingTests(unittest.TestCase):
    def test_builds_greeting(self) -> None:
        self.assertEqual(build_greeting("Codex"), "Welcome aboard, Codex!")

    def test_trims_name(self) -> None:
        self.assertEqual(build_greeting("  Traveler  "), "Welcome aboard, Traveler!")

    def test_rejects_blank_name(self) -> None:
        with self.assertRaises(ValueError):
            build_greeting("   ")


if __name__ == "__main__":
    unittest.main()
