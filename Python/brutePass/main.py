from pynput.keyboard import Key, Controller
from itertools import product
import time

def type_sentence(sentence, timeout, end_enter=True):
    for letter in sentence:
        keyboard.press(letter)
        keyboard.release(letter)
        time.sleep(0.1)
    
    if end_enter:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

def generate_combinations(characters, length):
    return [''.join(combination) for combination in product(characters, repeat=length)]

keyboard = Controller()

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

print("waiting")
time.sleep(3)
print("going")

for character in characters:
    print(character)

print(len(characters))
string_length = 22

combinations = generate_combinations(characters, string_length)

combos_len = len(combinations)
print(combos_len)
current_combo = 0

for combo in combinations[:10]:
    current_combo += 1
    print("testing combo: " + combo + ", # " + str(current_combo))
    type_sentence(combo, 0.05)

# type_sentence("hello!", 0.1)
