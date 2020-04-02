from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [25]
class Solution:

    # K个一组翻转列表
    @staticmethod
    def reverse_k_group(head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start:
            count = 0
            prev = start
            cur = start.next
            while cur and cur.next and count < k:
                count += 1
                cur.next, prev, cur = prev, cur, cur.next
            if count == k:
                start = prev
        return dummy.next


if __name__ == '__main__':
    test_head = generate_list_node([1, 2, 3, 4, 5])
    print_list_node(test_head)
    h = Solution.reverse_k_group(test_head, 2)
    print_list_node(h)

