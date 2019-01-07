import sys
import os
import pytest

print(os.getcwd())
from realtime import realtime_import


@realtime_import
def import_package():
    import package_for_test
    assert 'package_for_test' in sys.modules


def test_realtime_import():
    import_package()
    assert 'package_for_test' not in sys.modules
