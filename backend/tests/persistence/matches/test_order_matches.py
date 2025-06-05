from src.persistence.matches.order import order_matches_by_latest

def test_order_matches_by_latest():
    matches1 = [[1], [2], [3], [4]]
    matches2 = [[1], [2], [3], [4], [5]]


    order_matches_by_latest(matches1)
    order_matches_by_latest(matches2)
    assert matches1 == [[4], [3], [2], [1]]
    assert matches2 == [[5], [4], [3], [2], [1]]


test_order_matches_by_latest()