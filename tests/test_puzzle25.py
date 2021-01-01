from puzzles.puzzle25 import get_encryption_key


def test_part1():
    PUBLIC_KEY_CARD = 5764801
    PUBLIC_KEY_DOOR = 17807724
    key = get_encryption_key(PUBLIC_KEY_CARD, PUBLIC_KEY_DOOR)
    assert key == 14897079
