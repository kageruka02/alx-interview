#!/usr/bin/python3
"unlocking boxes"


def canUnlockAll(boxes):
    "unlocking boxes"
    push = set([0])
    display = set()
    for index in range(0, len(boxes) - 1):
        push.update(set(boxes[index]))
        for i in push:
            if i < len(boxes) and i >= 0:
                display.update(set(boxes[i]))
        if index + 1 not in display:
            return False
    return True
