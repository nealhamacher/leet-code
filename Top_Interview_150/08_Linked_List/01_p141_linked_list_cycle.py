# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    # Runtime: 1813 ms, beats 7.87%. Memory: 18.85 MB, beats 26.64
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        visited = []
        while current != None:
            if current in visited:
                return True
            else:
                visited.append(current)
                current = current.next
        return False

    # Using Floyd's tortoise and hare method
    # Runtime: 30 ms, beats 80.24%. Memory: 18.90, beats 26.64%
    def hasCycleFloyd(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = tortoise = head
        while hare != None and hare.next != None:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False


################################################################################
if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(sol.hasCycle(node1))
    print(sol.hasCycleFloyd(node1))

    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1
    print(sol.hasCycle(node1))
    print(sol.hasCycleFloyd(node1))

    node1 = ListNode(1)
    print(sol.hasCycle(node1))
    print(sol.hasCycleFloyd(node1))