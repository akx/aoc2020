from math import ceil


def decode_to_coords(bsp):
    x0 = y0 = 0
    y1 = 127
    x1 = 8
    for c in bsp:
        assert y1 >= y0
        if c == "F":
            y1 = y0 + (y1 - y0) // 2
        elif c == "B":
            y0 = y0 + ceil((y1 - y0) / 2)
        elif c == "L":
            x1 = x0 + (x1 - x0) // 2
        elif c == "R":
            x0 = x0 + ceil((x1 - x0) / 2)
    assert y1 - y0 <= 1
    assert x1 - x0 <= 1
    return min(x0, x1), min(y0, y1)


def coords_to_seat_id(coords):
    return coords[1] * 8 + coords[0]


def test_decode(bsp, real_coords, real_seat_id):
    coords = decode_to_coords(bsp)
    seat_id = coords_to_seat_id(coords)
    print(bsp, (coords, real_coords), (seat_id, real_seat_id))


if __name__ == "__main__":
    test_decode("FBFBBFFRLR", (5, 44), 357)
    test_decode("FFFBBBFRRR", (7, 14), 119)
    test_decode("BFFFBBFRRR", (7, 70), 567)
