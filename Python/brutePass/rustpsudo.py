def gen_combos(chars, length, current_combo):
    if length == 0:
        # no more to add, print/return combination
        print(current_combo)
        return
    
    for char in chars:
        # add next character to the current combination
        new_combo = current_combo + char

        # recursive call to generate combinations with the remaining length
        gen_combos(chars, length-1, new_combo)

characters = ["a", "b", "c", "d", "e", "f"]
string_length = 5

gen_combos(characters, string_length, "")