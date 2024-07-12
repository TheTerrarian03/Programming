from pathlib import Path

entries = Path("some_stuff/")
for entry in entries.iterdir():
    print(entry.name)

print("YAY!")
