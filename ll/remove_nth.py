'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Approach 1: Two pass algorithm
Intuition

We notice that the problem could be simply reduced to another one : Remove the (L - n + 1)(L−n+1) th node from the beginning in the list ,
where LL is the list length. This problem is easy to solve once we found list length LL.

Algorithm

First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases
such as a list with only one node, or removing the head of the list. On the first pass, we find the list length LL. 
Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L - n)(L−n) th node. 
We relink next pointer of the (L - n)(L−n) th node to the (L - n + 2)(L−n+2) th node and we are done.
Approach 2: One pass algorithm
Algorithm

The above algorithm could be optimized to one pass. 
Instead of one pointer, we could use two pointers. The first pointer advances the list by n+1n+1 steps from the beginning, 
while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by nn nodes apart. 
We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. 
The second pointer will be pointing at the nnth node counting from the last. 
We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head
            size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head
        
