# Split the cardsets into game identifier, an array of winning nums, and an array of pulled nums.
# As you walk down the array of pulled nums, compare each pulled num to the winning array. If there's a match,
# begin scoring. If score == 0, add 1; else, add 2.
# Assign point value to card. Once all cards have been read, total point values and add together.