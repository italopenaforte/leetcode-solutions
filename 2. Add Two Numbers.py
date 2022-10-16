from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def AddTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        num_l1, num_l2 = "", ""
        while(l1.next):
            num_l1 += str(l1.val)
            l1 = l1.next
        while(l2.next):
            num_l2 += str(l2.val)
            l2 = l2.next
            
        num_l1 += str(l1.val)
        num_l2 += str(l2.val)
        
        sum_ = int(num_l1[::-1]) + int(num_l2[::-1])
        
        tmp = return_ = ListNode(0)
        
        if sum_ == 0:
            return ListNode(0)
        while(sum_):
            print(sum_%10)
            tmp.next = ListNode(sum_%10)
            tmp = tmp.next
            sum_ //= 10
            
        return return_.next