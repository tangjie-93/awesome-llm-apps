from __future__ import annotations

import unittest

from security.permissions import can_access, normalize_groups


class PermissionTest(unittest.TestCase):
    def test_public_access(self) -> None:
        self.assertTrue(can_access(("public",), None))

    def test_group_access(self) -> None:
        self.assertTrue(can_access(("security", "ops"), ["ops"]))
        self.assertFalse(can_access(("security",), ["hr"]))

    def test_normalize_groups(self) -> None:
        self.assertEqual(normalize_groups([" Ops ", "ops", "security"]), ("ops", "security"))


if __name__ == "__main__":
    unittest.main()
