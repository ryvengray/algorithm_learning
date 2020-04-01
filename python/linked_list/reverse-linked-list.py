from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [206]
class Solution:

    # 反转链表 - 迭代的方法
    @staticmethod
    def reverse_list_iteration(head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    # 反转链表 - 递归形式
    @staticmethod
    def reverse_list_recursive(head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = Solution.reverse_list_recursive(head.next)
        # 认为当前节点前面的节点都已经反转完成
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    # Iteration
    h = generate_list_node([1, 2, 3, 4, 5])
    print_list_node(h)
    print('After:')
    h = Solution.reverse_list_iteration(h)
    print_list_node(h)

    # Recursive
    h = generate_list_node([1, 2, 3, 4, 5])
    print_list_node(h)
    print('After:')
    h = Solution.reverse_list_recursive(h)
    print_list_node(h)
