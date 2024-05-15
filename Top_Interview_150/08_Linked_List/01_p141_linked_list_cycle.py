# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        visited = [current]
        while current.next != None:
            if current.next in visited:
                return True
            else:
                current = current.next
                visited.append(current)
        return False

    # Using Floyd's tortoise and hare method
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