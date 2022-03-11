class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    
class Solution(object):
    def printList(self, l1):
        output = []

        while l1:
            output.append(l1.val)
            l1 = l1.next

        return output

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry%10)
            curr = curr.next

            carry //= 10
        print(self.printList(output))
        return output.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1,l2))