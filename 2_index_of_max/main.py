"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if numbers:
            max_index = numbers.index(max(numbers))
            print(max_index)
            return max_index
        else:
            print("list can not blank")
            return "list can not blank"


inputs = [int(i) for i in input("ใส่ตัวเลขแล้วเว้นวรรค: ").split()]
sol = Solution()
sol.find_max_index(inputs)
