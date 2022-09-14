import heapq as hq

class ListNode:
    """
    Class for nodes in linked list, which is I/O for mergeKLists().
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    Sort a list of linked list by storing their values in a array, sort the array and reconstruct a sorted linked list.
    Note this may not be the best implementation b/c we didn't use the property that each linked list in the input is sorted.
    
    Complexity analysis: n = total number nodes, k = number of linked list
    Time: O(n logn)
    Space: O(n)
    """
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


def mergeKLists(lists):
    """
    Sort a list of linked list by using a min heap of max size of k. This utilizes the property that each linked
    list is sorted.
    
    Complexity analysis:
    Time: O(n logk)
    Space: O(n), auxillary space is O(k), output is O(n)
    """
    # store the head of each linked list in heap
    ctr = 0
    heap = []
    for list in lists:
        hq.heappush(heap, (list.val, ctr, list))
        ctr += 1
    
    head = curr = ListNode(0)
    while heap:
        min_val, _, node = hq.heappop(heap)
        curr.next = ListNode(min_val)
        curr = curr.next
        ctr += 1
        if node.next:
            node = node.next
            hq.heappush(heap, (node.val, ctr, node))
    
    return head.next


def createKLists(arrays):
    """
    Utility function to create lists of linked list from list of arrays, used for creating input for mergeKLists().
    """
    lists = []
    for array in arrays:
        head = curr = ListNode(0)
        for num in array:
            curr.next = ListNode(num)
            curr = curr.next
        lists.append(head.next)
    return lists


def readList(list):
    """
    Utitlity function to create array from a linked list, used for testing the output of mergeKLists().
    """
    nums = []
    curr = list
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return nums


def test(arrays):
    """
    Utitlity function to test the correctness of mergeKLists().
    """
    lists = createKLists(arrays)
    list = mergeKLists(lists)
    array = readList(list)
    return array


if __name__ == "__main__":
    """
    Contain test cases for mergeKLists().
    """
    arrays = [[1,4,5],[1,3,4],[2,6]]
    print(test(arrays))