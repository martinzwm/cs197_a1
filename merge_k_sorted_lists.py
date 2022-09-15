"""
This file contains 2 approaches to merge k sorted linked list
and return a single sorted and merge linked list.
"""
import heapq as hq


class ListNode:
    """
    Class for nodes in linked list, which is I/O for merge_k_lists().
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """
    Sort a list of linked list by storing their values in a array, sort the
    array and reconstruct a sorted linked list.
    Note this may not be the best implementation b/c we didn't use the
    property that each linked list in the input is sorted.
    
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


def merge_k_lists_h(lists):
    """
    Sort a list of linked list by using a min heap of max size of k. This
    utilizes the property that each linked
    list is sorted.
    
    Complexity analysis:
    Time: O(n logk)
    Space: O(n), auxillary space is O(k), output is O(n)
    """
    # store the head of each linked list in heap
    ctr = 0
    heap = []
    for node in lists:
        hq.heappush(heap, (node.val, ctr, node))
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


def merge_k_lists_r(lists):
    """
    Sort a list of linked list by recursively sorting a subset number
    of linked list, similarly to merge sort.
    
    Complexity analysis:
    Time: O(n logk)
    Space: O(1), auxillary space is O(1), output is O(n)
    """
    # base case
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # recursive case
    partition = len(lists) // 2
    left_list = merge_k_lists_r(lists[:partition])
    right_list = merge_k_lists_r(lists[partition:])
    return merge(left_list, right_list)


def merge(left_node, right_node):
    """
    Utility function for merge_k_list_r(). Merge 2 sorted linked lists.
    Return a sorted linked list.
    """
    head = curr = ListNode(0)
    # iterate through 2 linked lists and add the smaller value to sorted linked list
    while left_node and right_node:
        if left_node.val < right_node.val:
            curr.next = left_node
            left_node = left_node.next
        else:
            curr.next = right_node
            right_node = right_node.next
        curr = curr.next
    
    # add the leftover nodes
    if left_node:
        curr.next = left_node
    else:
        curr.next = right_node
    return head.next


def create_k_lists(arrays):
    """
    Utility function to create lists of linked list from list of arrays, used
    for creating input for merge_k_lists().
    """
    lists = []
    for array in arrays:
        head = curr = ListNode(0)
        for num in array:
            curr.next = ListNode(num)
            curr = curr.next
        lists.append(head.next)
    return lists

def read_list(node):
    """
    Utitlity function to create array from a linked list, used for testing the
    output of merge_k_lists().
    """
    nums = []
    curr = node
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return nums


def test(arrays):
    """
    Utitlity function to test the correctness of merge_k_lists().
    """
    lists = create_k_lists(arrays)
    sorted_list = merge_k_lists_r(lists)
    array = read_list(sorted_list)
    return array


if __name__ == "__main__":
    test_case1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(test(test_case1))
    