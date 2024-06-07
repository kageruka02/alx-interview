#!/usr/bin/python3
"unlocking boxes"


def canUnlockAll(boxes):
    "unlocking boxes"
    display = set([0])
    for index in range(0, len(boxes) - 1):
        boxes[index].append(0)
        for i in set(boxes[index]):
            if i < len(boxes) and i >= 0:
                display.update(set(boxes[i]))
        if index + 1 not in display:
            return False
    return True
