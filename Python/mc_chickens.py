import pyperclip as pc


beginning = "/summon minecraft:chicken 3907.00 70.90 -205.59 {Passengers:[{id:\"minecraft:chicken\""
# beginning = "/summon minecraft:chicken ~2 ~ ~2 {Passengers:[{id:\"minecraft:chicken\""
addition = ",Passengers:[{id:\"minecraft:chicken\""
addition_end = "}]"
end = "}"

amount = int(input("How many chickens stacked? (1-?)\n$ "))

if (amount < 1):
    quit()

amount -= 1

total = beginning + (addition * amount) + (addition_end * (amount+1)) + end

print("")
print(total)
pc.copy(total)