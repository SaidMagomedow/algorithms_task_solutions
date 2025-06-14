# Task link https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list
# Merge Two Sorted Lists
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    RU: Алгоритм решения:
    - определяем временный dummy узел для линковки на него входящих нод
    - цикл while позволяет избежать случая когда list1 и list2 пусты
    - используя два указателя берем элемент с указателем из list1 и сравниваем с элементом list2.
    - в зависимости от сравнения линкуем либо list1 либо list2 с dummy
    - пройдя указателем по всем элементам сформируется связанный список из dummy->list1|list2->....
    - функция возвращает dummy.next где next это первый элемент из связанного списка
    Сложность:
    - O(n+m) где n и m это длины входящих массивов

    EN: Algorithm Explanation:
    - Solution Approach:
    - Initialize a temporary dummy node to serve as the starting point for linking the incoming nodes.
    - Use a while loop to handle cases where either list1 or list2 might be empty.
    - Compare nodes using two pointers:
    - Take the current node from list1 and compare it with the current node from list2.
    - Link the smaller node to dummy:
    - Depending on the comparison, link either list1 or list2 to the dummy node.
    - Traverse until all nodes are processed:
    - After iterating through all elements, a merged linked list is formed in the structure:
    - dummy → list1|list2 → ... → remaining_nodes.
    - Return dummy.next:
    - Since dummy is a placeholder, the actual merged list starts at dummy.next.
    Time Complexity: O(n + m)
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2.next = list2
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


