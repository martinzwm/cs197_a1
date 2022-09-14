class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    # stores the values of the nodes in a list
    node_vals = []
    for curr in lists:
        while curr:
            node_vals.append(curr.val)
            curr = curr.next
    
    # construct a new linked list based on the sorted list
    node_vals.sort()
    head = curr = ListNode(0)
    for val in node_vals:
        curr.next = ListNode(val)
        curr = curr.next
        
    return head.next


def createKLists(arrays):
    lists = []
    for array in arrays:
        head = curr = ListNode(0)
        for num in array:
            curr.next = ListNode(num)
            curr = curr.next
        lists.append(head)
    return lists