# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 is None or pHead2 is None:
            # 当有一个链表为空时返回不为空的链表
            return pHead2 if pHead1 is None else pHead1
        # 均不为空时定义一个链表作为合并单结果
        temp = ListNode(-1)
        res = temp
        while pHead2 is not None and pHead1 is not None:
            if pHead1.val >= pHead2.val:
                temp.next = pHead2
                pHead2 = pHead2.next
            else:
                temp.next = pHead1
                pHead1 = pHead1.next
            temp = temp.next
        temp.next = pHead2 if pHead2 is not None else pHead1
        return res

# write code here
