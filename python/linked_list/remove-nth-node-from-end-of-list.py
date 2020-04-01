from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [19]
class Solution:

    # 反转链表 - 迭代的方法
    @staticmethod
    def remove_nth_from_end(head: ListNode, n) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # 第一个指针
        first = head
        while first and n:
            first = first.next
            n -= 1
        follower = dummy
        while first:
            first = first.next
            follower = follower.next
        follower.next = follower.next.next
        return dummy.next


if __name__ == '__main__':
    # Iteration
    h = generate_list_node([1, 2, 3, 4, 5])
    print_list_node(h)
    print('After:')
    h = Solution.remove_nth_from_end(h, 0)
    print_list_node(h)
