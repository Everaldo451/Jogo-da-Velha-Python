import os
import sys

print(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from persistence.matches.test_order_matches import test_order_matches_by_latest

test_order_matches_by_latest()