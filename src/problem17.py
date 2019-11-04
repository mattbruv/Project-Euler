"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

# Please do not take my solution to this problem seriously
# This problem is a joke

words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

# I am not proud of this..
def numToWord(number):
    numString = str(number)
    word = ""

    # Hundreds
    if len(numString) == 4:
        return "onethousand"
    if len(numString) == 3:
        hundreds = words[int(numString[0])]
        word += hundreds + "hundred"
        if number % 100 == 0:
            return word
        else:
            word += "and"
        remainder = int(numString[1:3])
        word += numToWord(remainder)
    elif len(numString) == 2:
        if number >= 10 and number <= 20:
            word = words[int(numString)]
            return word
        tens = words[int(numString[0]) * 10]
        word += tens
        zeros = int(numString[1])
        if zeros != 0:
            word += numToWord(zeros)
        else:
            return word
    elif len(numString) == 1:
        return words[int(numString[0])]

    return word

def sumLetterRange(start, finish):
    string = ""
    for i in range(start, finish + 1):
        string += numToWord(i)
    return len(string)

print(sumLetterRange(1, 1000))

# 21124