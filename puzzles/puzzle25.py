def loop(val: int, subject_num: int = 7) -> int:
    val *= subject_num
    return val % 20201227


def get_encryption_key(PUBLIC_KEY_CARD: int, PUBLIC_KEY_DOOR: int) -> int:
    val = loop_size = 1
    while True:
        val = loop(val)
        if val == PUBLIC_KEY_CARD:
            break
        loop_size += 1

    key = 1
    for _ in range(loop_size):
        key = loop(key, PUBLIC_KEY_DOOR)

    return key


if __name__ == "__main__":

    PUBLIC_KEY_CARD = 3469259
    PUBLIC_KEY_DOOR = 13170438

    key = get_encryption_key(PUBLIC_KEY_CARD, PUBLIC_KEY_DOOR)
    print(key)
