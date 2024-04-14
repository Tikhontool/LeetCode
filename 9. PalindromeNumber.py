class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_list = list(str(x))
        list_reverse = input_list[::-1]
        if input_list == list_reverse:
            return True
        else:
            return False


s = Solution()
s.isPalindrome(121)
