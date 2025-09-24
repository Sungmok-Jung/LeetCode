# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(val=0, next=None)
        
        sub_l1 = l1
        sub_l2 = l2 # copy
        
        overflow = 0
        tmp = result
        while sub_l1 and sub_l2:
            sum_ = sub_l1.val + sub_l2.val + overflow
            if sum_ >= 10:
                overflow = 1
            else:
                overflow = 0
            target = sum_ % 10
            tmp.next = ListNode(val=target, next = None)
            tmp = tmp.next
            
            sub_l1 = sub_l1.next
            sub_l2 = sub_l2.next

        while sub_l1:
            sum_ = sub_l1.val + overflow
            if sum_ >= 10:
                overflow = 1
            else:
                overflow = 0
            target = sum_ % 10
            tmp.next = ListNode(target, next=None)
            tmp = tmp.next

            sub_l1 = sub_l1.next

        while sub_l2:
            sum_ = sub_l2.val + overflow
            if sum_ >= 10:
                overflow = 1
            else:
                overflow = 0
            target = sum_ % 10
            tmp.next = ListNode(target, next=None)
            tmp = tmp.next

            sub_l2 = sub_l2.next

        if overflow:
            tmp.next = ListNode(val=1, next=None)
        
        return result.next
