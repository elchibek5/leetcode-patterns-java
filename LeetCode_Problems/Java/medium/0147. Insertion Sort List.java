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
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode curr = head;

        while (curr != null) {
            ListNode prev = dummy;

            while (prev.next != null && prev.next.val < curr.val) {
                prev = prev.next;
            }

            ListNode nextTemp = curr.next;

            curr.next = prev.next;
            prev.next = curr;

            curr = nextTemp;
        }

        return dummy.next;

    }
}


// SECOND SOLUTION

// class Solution {
//     public ListNode insertionSortList(ListNode head) {
//         for (ListNode cur = head; cur != null; cur = cur.next) {
//             for (ListNode j = head; j != cur; j = j.next) {
//                 if (j.val > cur.val) {
//                     int t = j.val;
//                     j.val = cur.val;
//                     cur.val = t;
//                 }
//             }
//         }
//         return head;

//     }
// }
