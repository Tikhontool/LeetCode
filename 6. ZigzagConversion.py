# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R


# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Скорее всего лучше всего будет использовать какую-нибудь матрицу, где ее высота будет определяться кол-вом
        # строк. Проверка на возможен ли тот зигзаг, который нам предлагают
        # Изначально строить матрицу "шириной" 1, постепенно ее увеличивая
        # Матрицу можно создать с помощью вложенных массивов
        # Срезы возможно должны дополняться пустыми строками

        # Допустим, если длинна строки не делиться на цело на число строк, дополняем ее пустыми строками

        matrix = [[] for i in range(numRows)]
        switch = False
        y_index = 0
        result_str = ""

        for i in range(len(s)):
            matrix[y_index].append(s[i])
            if y_index == numRows - 1 or y_index == 0:
                switch = not switch
            if numRows > 1:
                if switch:
                    y_index = y_index + 1
                else:
                    y_index = y_index - 1
        for i in matrix:
            result_str = result_str + ''.join(i)

        return result_str


s = Solution()
# s.convert("A", 1)
s.convert("PAYPALISHIRING", 1)
# s.convert("PAYPALISHIRING", 3)
# s.convert("PAYPALISHIRING", 4)
# s.convert("PAYPALISHIRING", 5)
