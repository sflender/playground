import os
import sys

import sys
from pathlib import Path

# Add project root to sys.path for imports
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.stock import Store, restock_report


def test_restock_report_basic():
    store = Store()
    store.add_item('apple', 50)
    store.add_item('banana', 10)

    desired = {'apple': 100, 'banana': 20, 'orange': 5}
    report = restock_report(store, desired)

    assert report == {'apple': 50, 'banana': 10, 'orange': 5}
