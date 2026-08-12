"""
1 курс, вариант 1
Односвязный список целых чисел с удалением нечётных элементов.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def add(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self.len += 1

    def remove_odd(self):
        while self.head and self.head.val % 2 != 0:
            self.head = self.head.next
            self.len -= 1

        if not self.head:
            return

        cur = self.head
        while cur and cur.next:
            if cur.next.val % 2 != 0:
                cur.next = cur.next.next
                self.len -= 1
            else:
                cur = cur.next

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def __str__(self):
        if not self.head:
            return "[]"
        parts = []
        cur = self.head
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        return "[" + ", ".join(parts) + "]"
