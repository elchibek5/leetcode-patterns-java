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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                minHeap.add(lists[i]);
            }
        }
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        while(!minHeap.isEmpty()) {
            ListNode smallest = minHeap.poll();
            tail.next = smallest;
            tail = tail.next;

            if (smallest.next != null) {
                minHeap.add(smallest.next);
            }
        }
        return dummy.next;
    }
}

// SOLUTION 2: divide and conquer, merging pairs of lists

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
//     public ListNode mergeKLists(ListNode[] lists) {
//         if (lists == null || lists.length == 0) return null;

//         return solve(lists, 0, lists.length - 1);
//     }

//     public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
//         ListNode dummy = new ListNode(0);
//         ListNode curr = dummy;

//         while (l1 != null && l2 != null) {
//             if (l1.val <= l2.val) {
//                 curr.next = l1;
//                 l1 = l1.next;
//             } else {
//                 curr.next = l2;
//                 l2 = l2.next;
//             }
//             curr = curr.next;
//         }

//         if (l1 != null) curr.next = l1;
//         if (l2 != null) curr.next = l2;

//         return dummy.next;
//     }

//     public ListNode solve(ListNode[] lists, int left, int right) {
//         if (left == right) return lists[left];

//         int mid = left + (right - left) / 2;
        
//         ListNode l1 = solve(lists, left, mid);
//         ListNode l2 = solve(lists, mid + 1, right);

//         return mergeTwoLists(l1, l2);
//     }
// }
