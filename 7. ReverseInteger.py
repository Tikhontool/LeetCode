# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:

        minus = False
        number_list = list(str(x))

        if number_list[0] == "0" and len(number_list) > 1:
            number_list.pop(0)

        if number_list[0] == "-":
            number_list.pop(0)
            minus = True

        number_list.reverse()
        str_number = "".join(number_list)

        if minus:
            str_number = "-" + str_number

        int_number = int(str_number)
        if -(2 ** 31) <= int_number <= (2 ** 31) - 1:
            return int_number
        else:
            return 0


s = Solution()
print(s.reverse(123))
