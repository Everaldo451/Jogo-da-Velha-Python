from src.persistence.matches.order import order_matches_by_latest

def test_order_matches_by_latest():
    matches = [[1], [2], [3], [4]]
    ordered_matches_by_latest = [[4], [3], [2], [1]]

    assert order_matches_by_latest(matches) == ordered_matches_by_latest


test_order_matches_by_latest()