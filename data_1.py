file = open("data_1.txt")

line = file.readlines()

file.close()

print(line[2])

    # lines to read
line_numbers = [1, 3, 5, 7]
    # To store lines
lines = []
for i, line in enumerate(line):
    if i in line_numbers:
            lines.append(line.strip())
    elif i > 6:
            # don't read after line 7 to save time
        break
print(lines)

# Many ways to read a line see this- important https://pynative.com/python-read-specific-lines-from-a-file/