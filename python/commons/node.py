# 单链表
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def generate_list_node(arr):
    if len(arr) == 0:
        return None
    head, pre = None, None
    for v in arr:
        if head is None:
            head = ListNode(v)
            pre = head
        else:
            node = ListNode(v)
            pre.next = node
            pre = node
    return head


def print_list_node(head):
    node = head
    while node is not None:
        print(node.val, end='\t->\t')
        node = node.next
    print('null')
