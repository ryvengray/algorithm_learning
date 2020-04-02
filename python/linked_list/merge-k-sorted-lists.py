from python.commons.node import ListNode, generate_list_node, print_list_node
from queue import PriorityQueue


# leetcode [23]
class Solution:

    # 两数相加
    @staticmethod
    def merge_k_list(lists: [ListNode]) -> ListNode:
        # 傀儡
        dummy = ListNode(0)
        current = dummy

        p = PriorityQueue()
        import itertools
        counter = itertools.count(1)

        def put(li_node):
            p.put((li_node.val, next(counter), li_node))

        for li in lists:
            if li:
                put(li)

        while not p.empty():
            val, priority, node = p.get()
            current.next = node
            current = node
            node = node.next
            if node:
                put(node)

        return dummy.next


if __name__ == '__main__':
    # Iteration
    n1 = generate_list_node([2, 4, 8])
    n2 = generate_list_node([1, 2, 2, 3, 8, 9])
    n3 = generate_list_node([2, 5])
    print('Merge:')
    h = Solution.merge_k_list([n1, n2, n3])
    print_list_node(h)
