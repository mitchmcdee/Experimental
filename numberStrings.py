import unittest
from num2words import num2words

tiny = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
small = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
medium = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
big = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]

def numToString(num=None):
    length = len(str(num))
    digits = [int(n) for n in list(str(num))]
    nums = [str(e) + "0" * (length - i - 1) for i,e in enumerate(digits)]

    if type(num) != int:
       return "NaN"
    elif num < 10:
        return tiny[num]
    elif num < 20:
        return small[num - 10]
    elif num < 100:
        string = medium[digits[0]-2]
        if digits[1] == 0:
            return string
        else:
            return string + "-" + tiny[digits[1]]
    elif num < 1000:
        string = tiny[digits[0]] + " hundred"
        if all(n == 0 for n in digits[1:]):
            return string
        else:
            return string + " and " + str(numToString(int(str(num)[1:])))
    else:
        multiplier = ((length - 1) // 3) * 3

        string = str(numToString(int(str(num)[:-multiplier]))) + " " + big[(multiplier // 3) - 1]
        if all(n == 0 for n in digits[length-multiplier:]):
            return string
        elif all(n == 0 for n in digits[length-multiplier:-2]):
            string += " and "
        else:
            string += ", "
        return string + str(numToString(int(str(num)[length-multiplier:])))


class Test(unittest.TestCase):
    def testNumbers(self):
        for i in range(0, 10000000, 17):
            print(numToString(i))
            self.assertEqual(num2words(i), numToString(i))


if __name__ == "__main__":
    unittest.main()
