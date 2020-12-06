from d05lib import decode_to_coords, coords_to_seat_id

code_to_coords = {
    bsp: decode_to_coords(bsp) for bsp in open("../inputs/d05-input.txt") if bsp
}
code_to_seat_id = {
    bsp: coords_to_seat_id(coords) for (bsp, coords) in code_to_coords.items()
}
print(max(code_to_seat_id.values()))
