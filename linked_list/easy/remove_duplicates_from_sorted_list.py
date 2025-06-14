# task https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=problem-list-v2&envId=linked-list
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    RU: Алгоритм решения
    - определяем указатель cur, в первой итерации это head, но если не нашлось дупликатов, то указатель будет переключен на следующий элемент
    - если cur.val = cur.next.val, то есть следующий элемент это дупликат, то заменяем cur.next на cur.next.next, то есть удаляем cur.next с новой связью на следующий элемент
    - алгоритм работает только с отсортированного списка
    - если список не отсортирован, то советую воспользоваться хеш-маппой для того, что бы пометить элемент как дупликат
    Сложность алгоритма:
    - Time O(n), Space O(1)
    - если список не отсортирован - Time O(n), Space O(n)
    EN: Solution Algorithm
    - We initialize a pointer cur. On the first iteration, it starts at head, but if no duplicates are found, the pointer moves to the next node.
    - If cur.val == cur.next.val (i.e., the next node is a duplicate), we skip the duplicate by setting cur.next = cur.next.next, effectively removing cur.next and relinking to the next node.
    - This algorithm only works for sorted lists because duplicates must be adjacent.
    - For unsorted lists, it’s recommended to use a hash map to track duplicates efficiently.
    Time & Space Complexity:
    - Sorted List	Time O(n)	Space O(1)
    - Unsorted List Time O(n)	Space O(n)
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
