# Open the file for reading
f = open("deoo.txt", "r")

# Read the lines from the file
lines = f.readlines()

# Iterate over the lines and remove the newline character
lines = [line.rstrip('\n') for line in lines]

# Close the file
f.close()

# Open the file for writing
f = open("deoo.txt", "w")

# Write the modified lines
f.writelines(lines)

# Close the file
f.close()