"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def __init__(self):
        self.thai_number = (
            "ศูนย์",
            "หนึ่ง",
            "สอง",
            "สาม",
            "สี่",
            "ห้า",
            "หก",
            "เจ็ด",
            "แปด",
            "เก้า",
        )
        self.unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            print("number can not less than 0")
            return "number can not less than 0"
        if number == 0:
            print("ศูนย์")
            return "ศูนย์"
        if number > 10_000_000:
            return "number can not exceed 10,000,000"

        num_str = str(number)[::-1]
        result = ""

        for i, digit in enumerate(num_str):
            n = int(digit)
            if n == 0:
                continue

            if (
                i == 0 and n == 1 and len(num_str) > 1
            ):  # "เอ็ด" เฉพาะหลักหน่วย (ยกเว้นกรณีหลักเดียว)
                result = "เอ็ด" + result
            elif i == 1 and n == 2:  # "ยี่" สำหรับหลักสิบ
                result = "ยี่สิบ" + result
            elif i == 1 and n == 1:  # "สิบ" ไม่ต้องมี "หนึ่ง" ข้างหน้า
                result = "สิบ" + result
            elif i >= 6 and n == 1 and len(num_str) == 8:  # กรณี 10,000,000
                result = "สิบล้าน"
            else:
                result = self.thai_number[n] + self.unit[i] + result

        print(result)
        return result


num = int(input("ใส่ตัวเลข: "))
sol = Solution()
sol.number_to_thai(num)
