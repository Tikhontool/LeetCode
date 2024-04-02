# Given a string s, return the longest palindromic substring in s.


# Сложность моего алгоритма O(n^2) Для поиска палиндромов в строке можно использовать более эффективный алгоритм,
# например, алгоритм Манакера (Manacher's Algorithm), который имеет линейную сложность O(n). Алгоритм Манакера
# использует информацию о палиндромах, которые уже были найдены, чтобы эффективно продолжать поиск палиндромов в строке.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_mass = []
        mass_options = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                char_mass.append(s[j])
                char_str = ''.join(char_mass)
                char_str_reverse = ''.join(char_mass[::-1])
                if char_str == char_str_reverse:
                    mass_options.append(char_str)

            char_mass = []
        return max(mass_options, key=len)


s = Solution()
print(s.longestPalindrome(
    """zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"""))
# s.longestPalindrome("cbbd")
