#!/usr/bin/python3
"""Module determines the number of boxes that can be opened."""


def canUnlockAll(boxes):
    """Function determines the number of boxes that can be opened."""
    queue = []
    unique = set()
    unique.add(0)
    for i in boxes[0]:
        if i not in unique and i < len(boxes):
            unique.add(i)
            queue.append(i)

    while len(queue):
        for i in boxes[queue[0]]:
            if i not in unique and i < len(boxes):
                unique.add(i)
                queue.append(i)
        queue.pop(0)
    if len(unique) == len(boxes):
        return True
    return False
