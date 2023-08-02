from src import main


def test_get_last_operations():
    assert len(main.get_last_operations()) > 200
