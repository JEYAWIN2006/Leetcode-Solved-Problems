import java.util.*;

class Solution {
    public ListNode sortList(ListNode head) {
        List<Integer> list=new ArrayList<>();
        ListNode temp=head;
        while (temp != null){
            list.add(temp.val);
            temp = temp.next;
        }
        int[] arr = new int[list.size()];
        for (int i=0;i<list.size();i++) {
            arr[i]=list.get(i);
        }
        Arrays.sort(arr);
        ListNode dummy = new ListNode(0);
        ListNode curr=dummy;
        for (int num:arr) {
            curr.next=new ListNode(num);
            curr=curr.next;
        }
        return dummy.next;
    }
}