# open the file in read mode
file = open('demo.txt', 'r')

# read all lines from the file
lines = file.readlines()

# initialize the word count to 0
word_count = 0

# iterate over all the lines
for line in lines:
	# split the line into words
	words = line.split()

	# increment the word count
	word_count += len(words)

# print the total word count
print("Total word count =", word_count)

# close the file
file.close()