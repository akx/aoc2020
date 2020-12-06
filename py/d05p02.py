from d05lib import decode_to_coords, coords_to_seat_id

code_to_coords = {
    bsp: decode_to_coords(bsp) for bsp in open("../inputs/d05-input.txt") if bsp
}
code_to_seat_id = {
    bsp: coords_to_seat_id(coords) for (bsp, coords) in code_to_coords.items()
}

seats = set(code_to_seat_id.values())
min_seat = min(seats)
max_seat = max(seats)
for seat in range(min_seat, max_seat):
    if seat not in seats:
        print(seat)
