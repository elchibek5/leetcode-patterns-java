/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;

        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}

// SOLUTION 2 with recurtion

// /**
//  * Definition for singly-linked list.
//  * public class ListNode {
//  *     int val;
//  *     ListNode next;
//  *     ListNode() {}
//  *     ListNode(int val) { this.val = val; }
//  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//  * }
//  */
// class Solution {
//     ListNode start_point;

//     int rec(ListNode cur, ListNode parent, int n) {
//         if (cur == null) {
//             return 0;
//         } else {
//             int index_from_end = rec(cur.next, cur, n) + 1;
//             if (index_from_end == n) {
//                 if (cur == start_point) {
//                     start_point = cur.next;
//                 } else {
//                     parent.next = cur.next;
//                 }
//             }
//             return index_from_end;
//         }
//     }

//     public ListNode removeNthFromEnd(ListNode head, int n) {
//         start_point = head;
//         rec(head, null, n);
//         return start_point;
//     }
// }
