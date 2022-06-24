class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1
        if list1.val <= list2.val:
            answer = ListNode(list1.val)
            list1 = list1.next
        else:
            answer = ListNode(list2.val)
            list2 = list2.next
        copy = answer
        while list1 and list2:
            if list1.val <= list2.val:
                copy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                copy.next = ListNode(list2.val)
                list2 = list2.next
            copy = copy.next
        while list1:
            copy.next = ListNode(list1.val)
            list1 = list1.next
            copy = copy.next
        while list2:
            copy.next = ListNode(list2.val)
            list2 = list2.next
            copy = copy.next
        return answer