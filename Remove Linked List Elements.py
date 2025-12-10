# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy node to handle cases where head itself must be removed
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                # skip the current node
                prev.next = curr.next
            else:
                # move prev only when we don't delete curr
                prev = curr
            curr = curr.next

        return dummy.next
