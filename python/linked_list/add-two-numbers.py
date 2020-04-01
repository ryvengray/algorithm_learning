from python.commons.node import ListNode, generate_list_node, print_list_node


# leetcode [2]
class Solution:

    # 两数相加
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)
        cur = r
        carry = 0
        while l1 or l2:
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = v // 10
            cur.next = ListNode(v % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return r.next


if __name__ == '__main__':
    # Iteration
    n1 = generate_list_node([2, 4, 3])
    n2 = generate_list_node([5, 6, 4, 1])
    print('Calculate:')
    h = Solution.add_two_numbers(n1, n2)
    print_list_node(h)
