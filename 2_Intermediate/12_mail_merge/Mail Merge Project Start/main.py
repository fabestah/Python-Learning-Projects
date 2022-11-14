# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open(
    "Mail Merge Project Start/Input/Letters/starting_letter.txt"
) as starting_letter:
    s_letter = starting_letter.read()

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as inv_names:
    for x in inv_names.readlines():
        names.append(x.replace("\n", ""))

print(s_letter)
print(names)

for n in names:
    new_letter = s_letter.replace("[name]", n)
    new_path = f"Mail Merge Project Start/Output/ReadyToSend/letter_{n}.txt"
    for _ in range(len(names)):
        with open(new_path, "w") as letter:
            letter.write(new_letter)
