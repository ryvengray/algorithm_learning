from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [2]
class Solution:

    # 两数相加
    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
        # 傀儡
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                min_node = l1
                l1 = l1.next
            else:
                min_node = l2
                l2 = l2.next
            current.next = min_node
            current = min_node
        current.next = l1 if l1 else l2
        return dummy.next


if __name__ == '__main__':
    # Iteration
    n1 = generate_list_node([2, 4, 8])
    n2 = generate_list_node([1, 2, 2, 3, 8, 9])
    print('Merge:')
    h = Solution.merge_two_lists(n1, n2)
    print_list_node(h)
