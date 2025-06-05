import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from persistence.matches.test_order_matches import test_order_matches_by_latest
from persistence.matches.test_create_matches import test_create_match
from persistence.matches.test_read_matches import test_read_all_matches, test_3_latest_matches

test_order_matches_by_latest()
test_create_match()
test_read_all_matches()
test_3_latest_matches()