from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [24]
class Solution:

    # 两两交换链表中的节点
    @staticmethod
    def swap_pair(head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while pre and cur and cur.next:
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = cur

            pre = cur
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    test_head = generate_list_node([1])
    print_list_node(test_head)
    h = Solution.swap_pair(test_head)
    print_list_node(h)

