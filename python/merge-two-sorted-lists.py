from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # for easy printing
    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def merge_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


# Helper function: convert Python list → linked list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


# Create sample linked lists
list1 = build_linked_list([1, 3, 5, 7, 9])
list2 = build_linked_list([2, 4, 6, 8, 10])

# Merge them
s = Solution()
result = s.merge_lists(list1, list2)

# Print result
print(result)
