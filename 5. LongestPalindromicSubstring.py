# Given a string s, return the longest palindromic substring in s.


# Сложность моего алгоритма O(n^2) Для поиска палиндромов в строке можно использовать более эффективный алгоритм,
# например, алгоритм Манакера (Manacher's Algorithm), который имеет линейную сложность O(n). Алгоритм Манакера
# использует информацию о палиндромах, которые уже были найдены, чтобы эффективно продолжать поиск палиндромов в строке.


# Для каждого центра можно посчитать на каком максимальном размахе "крыла" строка является палиндромом
class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     char_mass = []
    #     mass_options = []
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             char_mass.append(s[j])
    #             char_str = ''.join(char_mass)
    #             char_str_reverse = ''.join(char_mass[::-1])
    #             if char_str == char_str_reverse:
    #                 mass_options.append(char_str)
    #
    #         char_mass = []
    #     return max(mass_options, key=len)

    def longestPalindrome_2(self, s):
        """
        Считаем палиндромы от центров
        :type s: str
        :rtype: str
        """

        mass_options = []
        if len(s) % 2 == 0:
            if len(s) != 0:
                for i in range(len(s) - 1):
                    left_center = i
                    right_center = i + 1
                    mass_options.append(s[left_center])

                    if s[left_center] == s[right_center]:
                        mass_options.append(f"{s[left_center] + s[right_center]}")

                    for step in range(1, i + 1):
                        if (right_center + step) < len(s) and s[left_center - step] == s[right_center + step]:
                            char_mass = str(s[left_center - step]) + s[left_center] + s[right_center] + str(
                                s[right_center + step])
                            mass_options.append(char_mass)
            else:
                return s
        else:
            if len(s) != 1:
                for i in range(1, len(s)):
                    char_mass = s[i]
                    for step in range(1, i + 1):
                        if (i + step) < len(s) and s[i - step] == s[i + step]:
                            char_mass = str(s[i - step]) + char_mass + str(s[i + step])
                            mass_options.append(char_mass)
            else:
                return s
        print("mass_options: ", mass_options)
        return max(mass_options, key=len)


s = Solution()
# print(s.longestPalindrome(
#     """zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"""))
s.longestPalindrome_2("babad")
s.longestPalindrome_2("cbbd")
s.longestPalindrome_2("ac")
s.longestPalindrome_2("abb")
