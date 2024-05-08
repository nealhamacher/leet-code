# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Carry digit
        carry = 0
        # Total Sum
        sum = []
        # Digits remaining in L1
        while l1 != None:
            # No digits remaining in L2, sum L1 digit and carry
            if l2 == None:
                current = l1.val + carry
                l1 = l1.next
            # Digits remaining in both, sum L1 digit, L2 digit, and carry
            else:
                current = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            # Determine if carrying a 1 and adjust current accordingly
            if current >= 10:
                carry = 1
                current -= 10
            else:
                carry = 0
            sum.append(current)

        # If L2 has more digits than L1
        while l2 != None:
            current = l2.val + carry
            if current >= 10:
                carry = 1
                current -= 10
            else:
                carry = 0
            sum.append(current)
            l2 = l2.next
        
        # Final carry 
        if carry == 1:
            sum.append(carry)

        return sum
    

################################################################################

if __name__ == "__main__":
    sol = Solution()
    l12 = ListNode(3)
    l11 = ListNode(4, l12)
    l10 = ListNode(2, l11)
    l22 = ListNode(4)
    l21 = ListNode(6, l22)
    l20 = ListNode(5, l21)
    print(sol.addTwoNumbers(l10, l20))
    l16 = ListNode(9)
    l15 = ListNode(9, l16)
    l14 = ListNode(9, l15)
    l13 = ListNode(9, l14)
    l12 = ListNode(9, l13)
    l11 = ListNode(9, l12)
    l10 = ListNode(9, l11)
    l23 = ListNode(9)
    l22 = ListNode(9, l23)
    l21 = ListNode(9, l22)
    l20 = ListNode(9, l21)
    print(sol.addTwoNumbers(l10, l20))
    print(sol.addTwoNumbers(l20, l10))
