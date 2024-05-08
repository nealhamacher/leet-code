# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        # Determine first value, lowest of list1 and list 3 value
        if list1.val <= list2.val:
            head = current = list1
            list1 = list1.next
        else:
            head = current = list2
            list2 = list2.next

        # Loop through while either list is not 0
        while list1 != None or list2 != None:
            # This if and elif are redundant I think 
            if list1 == None:
                current.next = list2
                break
            elif list2 == None:
                current.next = list1
                break
            else:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                    current = current.next
                else:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
        return head


################################################################################

if __name__ == "__main__":
    sol = Solution()
    l12 = ListNode(4)
    l11 = ListNode(2, l12)
    l10 = ListNode(1, l11)
    l22 = ListNode(4)
    l21 = ListNode(3, l22)
    l20 = ListNode(1, l21)
    head = sol.mergeTwoLists(l10, l20)
    while head != None:
        print(head.val)
        head = head.next
    print("\n")
    l10 = None
    l20 = ListNode(0)
    head = sol.mergeTwoLists(l10, l20)
    while head != None:
        print(head.val)
        head = head.next
    