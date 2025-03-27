"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            print("number can not less than 0")
            return "number can not less than 0"

        roman_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        result = ""

        for idx in sorted(roman_map.keys(), reverse=True):
            roman_digit = roman_map[idx]  # ดึงค่าเลขโรมัน

            times = number // idx
            number = number % idx
            result += roman_digit * times

        print(result)
        return result


num = int(input("ใส่ตัวเลข: "))
sol = Solution()
sol.number_to_roman(num)
