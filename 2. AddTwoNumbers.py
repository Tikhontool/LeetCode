# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def unpacker(self, list_objects, list_numbers):
        if list_objects.next is not None:
            list_numbers.append(list_objects.val)
            self.unpacker(list_objects.next, list_numbers)
        else:
            list_numbers.append(list_objects.val)
        return list_numbers

    def convertArrayToNumber(self, arrray):
        number = ""
        for i in arrray:
            number = number + str(i)
        return int(number)

    def addListNode(self, data):

        if self.head is None:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)
        print(self.head)

    def addTwoNumbers(self, l1, l2):

        # Распаковка связынных списков
        l1_number = self.unpacker(l1, [])[::-1]
        l2_number = self.unpacker(l2, [])[::-1]

        # Теперь эти массивы нужно развернуть и превратить в числа
        l1_number = self.convertArrayToNumber(l1_number)
        l2_number = self.convertArrayToNumber(l2_number)

        # Теперь эти массивы слудует переверунть
        mass_int = [int(i) for i in str(l1_number + l2_number)][::-1]
        self.head = None
        for i in mass_int:
            self.addListNode(i)
        return self.head
