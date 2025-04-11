from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, None))
print(courses)


def last(head: Node) -> int:
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)  # Recursive case


print(last(courses))
