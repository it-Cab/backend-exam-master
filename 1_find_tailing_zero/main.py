"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        count = 0
        if number < 0:
            print("number can not be negative")
            return "number can not be negative"

        divisor = 5
        while number >= divisor:
            count += number // divisor
            divisor *= 5

        print(count)
        return count


num = int(input("ใส่ตัวเลข: "))
sol = Solution()
sol.find_tailing_zeroes(num)
