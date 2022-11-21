class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

import sys
input = sys.stdin.readline().rstrip

def init_node_list():
    vals = map(int, input().split())

    head = curr = ListNode()

    for val in vals:
        curr.next = ListNode(val)
        curr = curr.next

    return head.next

def reverse_node_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

def print_node_list(head):
    runner = head

    while runner:
        print(runner.val, end=" ")
        runner = runner.next
    print()
        
head = init_node_list()
print('origin:   ', end=" ")
print_node_list(head)

head = reverse_node_list(head)
print('reversed: ', end=" ")
print_node_list(head)