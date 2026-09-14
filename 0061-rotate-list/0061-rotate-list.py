
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        tmp=head
        while tmp:
            arr.append(tmp.val)
            tmp=tmp.next
        k=k%len(arr)
        arr[:]=arr[-k:]+arr[:-k]
        node=ListNode(0)
        tmp=node
        for i in arr:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return node.next
        