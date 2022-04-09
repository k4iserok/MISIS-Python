class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f'{self.value}'


def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur)
        cur = cur.next


h, a, b, c, d, e = Node(2), Node(4), Node(1), Node(1), Node(2), Node(0)

h.next = a
a.next = b
b.next = c
c.next = d
d.next = e

print_linked_list(h)
print(f'')


def sort_linked_list(head):
    end = None
    while end != head:
        p = head
        while p.next != end:
            q = p.next
            if p.value > q.value:
                p.value, q.value = q.value, p.value
            p = p.next
        end = p


sort_linked_list(h)
print_linked_list(h)
