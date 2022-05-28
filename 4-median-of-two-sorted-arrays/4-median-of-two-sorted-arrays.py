class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        r1 = len(nums1)//2
        l2 = (len(nums2)-1)//2
        start = l2-(len(nums1)+1)//2
        end = l2+r1+1
        ptr1 = -1000000 if r1 == 0 else nums1[r1-1]
        ptr2 = 1000000 if l2+1 >= len(nums2) else nums2[l2+1]
        ptr3 = -1000000 if l2 < 0 else nums2[l2]
        ptr4 = 1000000 if r1 >= len(nums1) else nums1[r1]
        while ptr1 > ptr2 or ptr3 > ptr4:
            if ptr1 > ptr2:
                start = l2-1
                l2 = (l2+end)//2
            if ptr3 > ptr4:
                end = l2+1
                l2 = (l2+start)//2

            r1 = len(nums1)//2+(len(nums2)-1)//2-l2

            ptr1 = -1000000 if r1 <= 0 else nums1[r1-1]
            ptr2 = 1000000 if l2+1 >= len(nums2) else nums2[l2+1]
            ptr3 = -1000000 if l2 < 0 else nums2[l2]
            ptr4 = 1000000 if r1 >= len(nums1) else nums1[r1]
         
        start = max(ptr1, ptr3)
        end = min(ptr2, ptr4)
        
        if (len(nums1)+len(nums2))%2==0: return (start+end)/2
        elif len(nums1)%2==1: return end
        else: return start